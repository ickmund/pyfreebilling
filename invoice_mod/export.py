# -*- coding: utf-8 -*-
# Copyright 2013 Mathias WOLFF
# This file is part of pyfreebilling.
#
# pyfreebilling is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfreebilling is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfreebilling.  If not, see <http://www.gnu.org/licenses/>

import re
import datetime

from import_export import resources, fields

from yawdadmin.utils import get_option

from invoice.models import Invoice, InvoicePayment



class InvoiceResource(resources.ModelResource):
    """
    Export each invoice since the beginning of the year including payment
    """

    total = fields.Field(column_name='total')
    date_reglement = fields.Field(column_name='date_reglement')
    type_reglement = fields.Field(column_name='type_reglement')

    def dehydrate_total(self, invoice):
        return invoice.total()

    def dehydrate_date_reglement(self, invoice):
        payments = invoice.payments.order_by('-paid_date')
        if payments:
            return "%s" % payments[0].paid_date
        else:
            return ""

    def dehydrate_type_reglement(self, invoice):
        payments = invoice.payments.order_by('-paid_date')
        if payments:
            return payments[0].method
        else:
            return ""

    class Meta:
        model = Invoice
        fields = (
            'recipient__name',
            'invoice_id',
            'invoice_date',
            'invoice_cost_code',
            'is_credit_note',
            'invoice_related__invoice_id',
            'total',
            'is_paid',
            'date_reglement',
            'type_reglement')
        export_order = (
            'recipient__name',
            'invoice_id',
            'invoice_date',
            'invoice_cost_code',
            'is_credit_note',
            'invoice_related__invoice_id',
            'total',
            'is_paid',
            'date_reglement',
            'type_reglement')
        widgets = {
                'date_reglement': {'format': '%d.%m.%Y'},
                }


def gather_data_and_update_flags(test=False):
    invoices = Invoice.objects.filter(is_exported__in=('invoice_only',
                                                       'no'))

    code_ana_cotis = get_option('accounting_options', 'code_ana_cotisation')
    list_code_ana_sem = []
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_1'))
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_2'))
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_3'))
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_4'))

    data = []
    invoice_exported = []
    payments_exported = []
    for invoice in invoices:

        # Neither the invoice nor the payments have been exported
        # First we export the invoice
        if invoice.is_exported == 'no':
            if invoice.invoice_cost_code == code_ana_cotis:
                row_credit, row_debit = get_row_cotis(invoice)
            elif invoice.invoice_cost_code in list_code_ana_sem:
                row_credit, row_debit = get_row_seminaire(invoice)
            else:
                row_credit, row_debit = get_row_std_inv(invoice)
            data.append(row_credit)
            data.append(row_debit)
            invoice_exported.append(invoice)

        # Export the payments if there is some
        if invoice.payments.all():
            for payment in invoice.payments.all():
                row_credit, row_debit = get_row_payment(payment)
                data.append(row_credit)
                data.append(row_debit)
                payments_exported.append(payment)

    #
    # Update is_exported flag for invoices and payments
    #
    if not test:
        # We update all exported payment
        for payment in payments_exported:
            payment.is_exported = True
            payment.save()

        # We loop over all the invoices not exported or 'invoice_only'.
        # When only the invoice is exported, you can need to update
        # 'is_exported' if all the payments are exported
        for invoice in invoices:
            if invoice.is_paid:
                if invoice.is_credit_note:
                    # Credit note
                    invoice.is_exported = 'yes'
                elif hasattr(invoice, 'credit_note'):
                    # Invoice with a credit note
                    invoice.is_exported = 'yes'
                else:
                    # Standart invoice
                    are_payments_all_exported = True
                    for payment in invoice.payments.all():
                        if not payment.is_exported:
                            are_payments_all_exported = False
                    if are_payments_all_exported:
                        invoice.is_exported = 'yes'
                    else:
                        invoice.is_exported = 'invoice_only'
            else:
                invoice.is_exported = 'invoice_only'

            invoice.save()

    return data


def get_row_cotis(invoice):
    date = invoice.invoice_date.strftime('%d%m%Y')
    client = re.search(r'^411-(.+)', invoice.recipient.client_code).groups()[0]
    label = u"%s-cot" % invoice.recipient.name[:31]  # label max size: 35

    if invoice.is_credit_note:
        total = invoice.total() * -1
    else:
        total = invoice.total()

    row_credit = ['A1', date, 'VE', '756', '000', 'C', total, label,
                  invoice.invoice_id, invoice.invoice_cost_code, ]
    row_debit = ['G', date, 'VE', '411', client, 'D', total, label,
                 invoice.invoice_id, ]
    return row_credit, row_debit


def get_row_seminaire(invoice):
    date = invoice.invoice_date.strftime('%d%m%Y')
    client = re.search(r'^411-(.+)', invoice.recipient.client_code).groups()[0]
    label = u"%s-sém" % invoice.recipient.name[:31]  # label max size: 35

    if invoice.is_credit_note:
        total = invoice.total() * -1
    else:
        total = invoice.total()

    row_credit = ['A1', date, 'VE', '706', '200', 'C', total, label,
                  invoice.invoice_id, invoice.invoice_cost_code, ]
    row_debit = ['G', date, 'VE', '411', client, 'D', total, label,
                 invoice.invoice_id, ]
    return row_credit, row_debit


def get_row_std_inv(invoice):
    raise Exception(u"L'export ne support pas les factures ayant un code "
                    u"analytique autre que celui de cotisation ou d'un "
                    u"séminaire. (facture %s)" % invoice.invoice_id)


def get_row_payment(payment):
    date = payment.paid_date.strftime('%d%m%Y')
    client = re.search(r'^411-(.+)',
                       payment.invoice.recipient.client_code).groups()[0]
    # label max size: 35
    label = u"%s-rglt" % payment.invoice.recipient.name[:31]

    row_credit = ['G', date, 'BA', '411', client, 'C', payment.amount, label,
                  payment.invoice.invoice_id]
    row_debit = ['G', date, 'BA', '512', '000', 'D', payment.amount, label,
                 payment.invoice.invoice_id]
    return row_credit, row_debit


def export_annuel_gather_data():
    """ export annee courante - du 0101 a la date du jour """
    """ toutes les factures """
    #invoices = Invoice.objects.filter(is_exported='no')
    #invoices = invoices.
    invoices = Invoice.objects.filter(invoice_date__year=datetime.date.today().year)

    #import pdb; pdb.set_trace()

    code_ana_cotis = get_option('accounting_options', 'code_ana_cotisation')
    list_code_ana_sem = []
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_1'))
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_2'))
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_3'))
    list_code_ana_sem.append(get_option('accounting_options',
                                        'code_ana_seminaire_4'))

    data = []
    invoice_exported = []
    payments_exported = []
    for invoice in invoices:

        if invoice.invoice_cost_code == code_ana_cotis:
            row_credit, row_debit = get_row_cotis(invoice)
        elif invoice.invoice_cost_code in list_code_ana_sem:
            row_credit, row_debit = get_row_seminaire(invoice)
        else:
            row_credit, row_debit = get_row_std_inv(invoice)
        data.append(row_credit)
        data.append(row_debit)
        invoice_exported.append(invoice)

        # Export the payments if there is some
        if invoice.payments.all():
            for payment in invoice.payments.all():
                row_credit, row_debit = get_row_payment(payment)
                data.append(row_credit)
                data.append(row_debit)
                payments_exported.append(payment)

    return data