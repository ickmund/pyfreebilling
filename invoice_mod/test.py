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

from django.test import TestCase

from datetime import date
from decimal import Decimal

from invoice.models import Invoice, InvoiceItem, InvoicePayment
from pyfreebill.models import Company

from .export import get_row_cotis, get_row_seminaire, get_row_std_inv,\
    get_row_payment, gather_data_and_update_flags


class RowCase(TestCase):

    def test_row_cotisation_single_item(self):
        """
        Row cotisation
        """
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '90100'
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()

        row_credit, row_debit = get_row_cotis(invoice)
        today = date.today().strftime('%d%m%Y')
        self.assertEqual(row_credit, ['A1', today, 'VE', '756', '000', 'C',
                                      Decimal('350.00'), "MyCompany-cot",
                                      invoice.invoice_id, '90100'])
        self.assertEqual(row_debit, ['G', today, 'VE', '411', 'MYCO01',
                                     'D', Decimal('350.00'), "MyCompany-cot",
                                     invoice.invoice_id])

    def test_row_cotisation_multiple_items(self):
        """
        Row cotisation
        """
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '90100'
        item1 = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                            unit_price="350", quantity="1")
        item2 = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                            unit_price="500", quantity="2")
        item1.save()
        item2.save()

        row_credit, row_debit = get_row_cotis(invoice)
        today = date.today().strftime('%d%m%Y')
        self.assertEqual(row_credit, ['A1', today, 'VE', '756', '000', 'C',
                                      Decimal('1350.00'), "MyCompany-cot",
                                      invoice.invoice_id, '90100'])
        self.assertEqual(row_debit, ['G', today, 'VE', '411', 'MYCO01',
                                     'D', Decimal('1350.00'), "MyCompany-cot",
                                     invoice.invoice_id])

    def test_row_cotisation_length_label(self):
        """
        Max length of label: 35
        """
        invoice = self.get_blank_invoice(
            orga_name=u"CUSTOMER OUEST")
        invoice.invoice_cost_code = '90100'
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()

        row_credit, row_debit = get_row_cotis(invoice)
        self.assertLessEqual(len(row_credit[7]), '35')
        self.assertEqual(row_credit[7][-4:], '-cot')
        self.assertLessEqual(len(row_debit[7]), '35')
        self.assertEqual(row_debit[7][-4:], '-cot')

    def test_row_seminaire_length_label(self):
        """
        Max length of label: 35
        """
        invoice = self.get_blank_invoice(
            orga_name=u"CUSTOMER OUEST")
        invoice.invoice_cost_code = '01010'
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()

        row_credit, row_debit = get_row_seminaire(invoice)
        self.assertLessEqual(len(row_credit[7]), '35')
        self.assertEqual(row_credit[7][-4:], u'-sém')
        self.assertLessEqual(len(row_debit[7]), '35')
        self.assertEqual(row_debit[7][-4:], u'-sém')

    def test_row_payment_length_label(self):
        """
        Max length of label: 35
        """
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '01010'
        payment = InvoicePayment(invoice=invoice, amount=350,
                                 paid_date=date.today())
        payment.save()

        row_credit, row_debit = get_row_payment(payment)
        self.assertLessEqual(len(row_credit[7]), '35')
        self.assertEqual(row_credit[7][-5:], '-rglt')
        self.assertLessEqual(len(row_debit[7]), '35')
        self.assertEqual(row_debit[7][-5:], '-rglt')

    def test_row_seminaire_single_item(self):
        """
        Row séminaire
        """
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '01010'
        item = InvoiceItem(invoice=invoice, description="Séminaire",
                           unit_price="350", quantity="1")
        item.save()

        row_credit, row_debit = get_row_seminaire(invoice)
        today = date.today().strftime('%d%m%Y')
        self.assertEqual(row_credit, ['A1', today, 'VE', '706', '200', 'C',
                                      Decimal('350.00'), u"MyCompany-sém",
                                      invoice.invoice_id, '01010'])
        self.assertEqual(row_debit, ['G', today, 'VE', '411', 'MYCO01',
                                     'D', Decimal('350.00'), u"MyCompany-sém",
                                     invoice.invoice_id])

    def test_row_seminaire_multiple_items(self):
        """
        Row séminaire
        """
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '01010'
        item1 = InvoiceItem(invoice=invoice, description="Séminaire",
                            unit_price="350", quantity="1")
        item2 = InvoiceItem(invoice=invoice, description="Séminaire",
                            unit_price="400", quantity="2")
        item1.save()
        item2.save()

        row_credit, row_debit = get_row_seminaire(invoice)
        today = date.today().strftime('%d%m%Y')
        self.assertEqual(row_credit, ['A1', today, 'VE', '706', '200', 'C',
                                      Decimal('1150.00'), u"MyCompany-sém",
                                      invoice.invoice_id, '01010'])
        self.assertEqual(row_debit, ['G', today, 'VE', '411', 'MYCO01',
                                     'D', Decimal('1150.00'), u"MyCompany-sém",
                                     invoice.invoice_id])

    def test_row_std_inv(self):
        """
        Row standard invoice
        """
        invoice = self.get_blank_invoice()
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()
        self.assertRaises(Exception, get_row_std_inv, invoice)

    def test_row_payment(self):
        """
        Row paiement
        """
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '01010'
        payment = InvoicePayment(invoice=invoice, amount=350,
                                 paid_date=date.today())
        payment.save()

        row_credit, row_debit = get_row_payment(payment)
        today = date.today().strftime('%d%m%Y')
        self.assertEqual(row_credit, ['G', today, 'BA', '411', 'MYCO01', 'C',
                                      Decimal('350.00'), "MyCompany-rglt",
                                      invoice.invoice_id])
        self.assertEqual(row_debit, ['G', today, 'BA', '512', '000',
                                     'D', Decimal('350.00'), "MyCompany-rglt",
                                     invoice.invoice_id])

    def get_blank_invoice(self, orga_name="MyCompany"):
        """
        Create a blank invoice
        """
        college = College(name="DSI")
        college.save()
        orga = Organization(name=orga_name, college=college,
                            street="rue dans Nantes",
                            postal_code="44000", city="NANTES Cedex 4")
        orga.save()
        invoice = Invoice(recipient=orga, invoice_date=date.today())
        invoice.save()
        return invoice


class GatherDataCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # Imports must stay here
        from yawdadmin.models import AppOption
        from yawdadmin import admin_site
        from MYCouest.admin import AccountingOptions

        admin_site.register_options(AccountingOptions)
        AppOption.objects.filter(
            optionset_label='accounting_options',
            name='code_ana_cotisation').update(value='90100')
        AppOption.objects.filter(
            optionset_label='accounting_options',
            name='code_ana_seminaire_1').update(value='01010')
        AppOption.objects.filter(
            optionset_label='accounting_options',
            name='code_ana_seminaire_2').update(value='01020')
        AppOption.objects.filter(
            optionset_label='accounting_options',
            name='code_ana_seminaire_3').update(value='01030')
        AppOption.objects.filter(
            optionset_label='accounting_options',
            name='code_ana_seminaire_4').update(value='01040')

    def test_single_invoice_cotis(self):
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '90100'
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 2)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(data[0], ['A1', today, 'VE', '756', '000', 'C',
                                   Decimal('350.00'), "MyCompany-cot",
                                   invoice.invoice_id, '90100'])
        self.assertEqual(data[1], ['G', today, 'VE', '411', 'MYCO01',
                                   'D', Decimal('350.00'), "MyCompany-cot",
                                   invoice.invoice_id])
        self.assertEqual(invoice.is_exported, 'invoice_only')

    def test_single_invoice_seminaire(self):
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '01040'
        item = InvoiceItem(invoice=invoice, description="Séminaire normes",
                           unit_price="200", quantity="1")
        item.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 2)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(data[0], ['A1', today, 'VE', '706', '200', 'C',
                                   Decimal('200.00'), u"MyCompany-sém",
                                   invoice.invoice_id, '01040'])
        self.assertEqual(data[1], ['G', today, 'VE', '411', 'MYCO01',
                                   'D', Decimal('200.00'), u"MyCompany-sém",
                                   invoice.invoice_id])
        self.assertEqual(invoice.is_exported, 'invoice_only')

    def test_invoice_and_credit_note(self):
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '01040'
        item = InvoiceItem(invoice=invoice, description="Séminaire",
                           unit_price="200", quantity="1")
        item.save()
        credit_note = self.get_blank_invoice(inv_is_credit_note=True,
                                             inv_invoice_related=invoice)
        credit_note.invoice_cost_code = '01040'
        item2 = InvoiceItem(invoice=credit_note, description="Séminaire",
                            unit_price="200", quantity="1")
        item2.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)
        credit_note = Invoice.objects.get(pk=credit_note.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 4)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(data[0], ['A1', today, 'VE', '706', '200', 'C',
                                   Decimal('200.00'), u"MyCompany-sém",
                                   invoice.invoice_id, '01040'])
        self.assertEqual(data[1], ['G', today, 'VE', '411', 'MYCO01',
                                   'D', Decimal('200.00'), u"MyCompany-sém",
                                   invoice.invoice_id])
        self.assertEqual(invoice.is_exported, 'yes')
        self.assertEqual(data[2], ['A1', today, 'VE', '706', '200', 'C',
                                   Decimal('-200.00'), u"MyCompany-sém",
                                   credit_note.invoice_id, '01040'])
        self.assertEqual(data[3], ['G', today, 'VE', '411', 'MYCO01',
                                   'D', Decimal('-200.00'), u"MyCompany-sém",
                                   credit_note.invoice_id])
        self.assertEqual(credit_note.is_exported, 'yes')

    def test_credit_note_only(self):
        invoice = self.get_blank_invoice(inv_is_exported='invoice_only')
        invoice.invoice_cost_code = '01040'
        item = InvoiceItem(invoice=invoice, description="Séminaire",
                           unit_price="200", quantity="1")
        item.save()
        credit_note = self.get_blank_invoice(inv_is_credit_note=True,
                                             inv_invoice_related=invoice)
        credit_note.invoice_cost_code = '01040'
        item2 = InvoiceItem(invoice=credit_note, description="Séminaire",
                            unit_price="200", quantity="1")
        item2.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)
        credit_note = Invoice.objects.get(pk=credit_note.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 2)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(invoice.is_exported, 'yes')
        self.assertEqual(data[0], ['A1', today, 'VE', '706', '200', 'C',
                                   Decimal('-200.00'), u"MyCompany-sém",
                                   credit_note.invoice_id, '01040'])
        self.assertEqual(data[1], ['G', today, 'VE', '411', 'MYCO01',
                                   'D', Decimal('-200.00'), u"MyCompany-sém",
                                   credit_note.invoice_id])
        self.assertEqual(credit_note.is_exported, 'yes')

    def test_one_invoice_and_one_already_exported(self):
        invoice1 = self.get_blank_invoice()
        invoice1.invoice_cost_code = '90100'
        invoice1.save()
        item1 = InvoiceItem(invoice=invoice1, description="Adhésion 2013",
                            unit_price="350", quantity="1")
        item1.save()
        invoice2 = self.get_blank_invoice(inv_is_exported='yes')
        invoice2.invoice_cost_code = '90100'
        item2 = InvoiceItem(invoice=invoice2, description="Adhésion 2014",
                            unit_price="350", quantity="1")
        item2.save()

        data = gather_data_and_update_flags(test=False)
        # We get invoice a second time since they have been modified by
        # gather_data_and_update_flags()
        invoice1 = Invoice.objects.get(pk=invoice1.pk)
        invoice2 = Invoice.objects.get(pk=invoice2.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 2)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(data[0], ['A1', today, 'VE', '756', '000', 'C',
                                   Decimal('350.00'), "MyCompany-cot",
                                   invoice1.invoice_id, '90100'])
        self.assertEqual(data[1], ['G', today, 'VE', '411', 'MYCO01',
                                   'D', Decimal('350.00'), "MyCompany-cot",
                                   invoice1.invoice_id])
        self.assertEqual(invoice1.is_exported, 'invoice_only')
        self.assertEqual(invoice2.is_exported, 'yes')

    def test_no_invoice(self):
        data = gather_data_and_update_flags(test=False)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 0)

    def test_no_invoice_to_export(self):
        invoice = self.get_blank_invoice(inv_is_exported='yes')
        invoice.invoice_cost_code = '90100'
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 0)
        self.assertEqual(invoice.is_exported, 'yes')

    def test_single_payment_full(self):
        invoice = self.get_blank_invoice(inv_is_exported='invoice_only')
        invoice.invoice_cost_code = '90100'
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()
        payment = InvoicePayment(invoice=invoice, amount=350,
                                 paid_date=date.today())
        payment.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)
        payment = InvoicePayment.objects.get(pk=payment.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 2)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(data[0], ['G', today, 'BA', '411', 'MYCO01', 'C',
                                   Decimal('350.00'), "MyCompany-rglt",
                                   invoice.invoice_id])
        self.assertEqual(data[1], ['G', today, 'BA', '512', '000',
                                   'D', Decimal('350.00'), "MyCompany-rglt",
                                   invoice.invoice_id])
        self.assertEqual(invoice.is_exported, 'yes')
        self.assertTrue(payment.is_exported)

    def test_single_payment_part(self):
        invoice = self.get_blank_invoice(inv_is_exported='invoice_only')
        invoice.invoice_cost_code = '90100'
        item = InvoiceItem(invoice=invoice, description="Adhésion 2014",
                           unit_price="350", quantity="1")
        item.save()
        payment = InvoicePayment(invoice=invoice, amount=200,
                                 paid_date=date.today())
        payment.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)
        payment = InvoicePayment.objects.get(pk=payment.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 2)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(data[0], ['G', today, 'BA', '411', 'MYCO01', 'C',
                                   Decimal('200.00'), "MyCompany-rglt",
                                   invoice.invoice_id])
        self.assertEqual(data[1], ['G', today, 'BA', '512', '000',
                                   'D', Decimal('200.00'), "MyCompany-rglt",
                                   invoice.invoice_id])
        # Since the payment doesn't pay for all the invoice, we put the flag at
        # 'invoice_only' waiting for new payments to export
        self.assertEqual(invoice.is_exported, 'invoice_only')
        self.assertTrue(payment.is_exported)

    def test_single_invoice_seminaire_and_payment(self):
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = '01040'
        item = InvoiceItem(invoice=invoice, description="Séminaire normes",
                           unit_price="200", quantity="1")
        item.save()
        payment = InvoicePayment(invoice=invoice, amount=200,
                                 paid_date=date.today())
        payment.save()
        data = gather_data_and_update_flags(test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)
        payment = InvoicePayment.objects.get(pk=payment.pk)

        self.assertIsNotNone(data)

        self.assertEqual(len(data), 4)

        today = date.today().strftime('%d%m%Y')
        self.assertEqual(data[0], ['A1', today, 'VE', '706', '200', 'C',
                                   Decimal('200.00'), u"MyCompany-sém",
                                   invoice.invoice_id, '01040'])
        self.assertEqual(data[1], ['G', today, 'VE', '411', 'MYCO01',
                                   'D', Decimal('200.00'), u"MyCompany-sém",
                                   invoice.invoice_id])
        self.assertEqual(data[2], ['G', today, 'BA', '411', 'MYCO01', 'C',
                                   Decimal('200.00'), "MyCompany-rglt",
                                   invoice.invoice_id])
        self.assertEqual(data[3], ['G', today, 'BA', '512', '000',
                                   'D', Decimal('200.00'), "MyCompany-rglt",
                                   invoice.invoice_id])
        self.assertEqual(invoice.is_exported, 'yes')
        self.assertTrue(payment.is_exported)

    def test_single_std_invoice(self):
        invoice = self.get_blank_invoice()
        invoice.invoice_cost_code = 'XXXX'
        item = InvoiceItem(invoice=invoice, description="Séminaire normes",
                           unit_price="200", quantity="1")
        item.save()
        payment = InvoicePayment(invoice=invoice, amount=200,
                                 paid_date=date.today())
        payment.save()

        self.assertRaises(Exception, gather_data_and_update_flags, test=False)
        invoice = Invoice.objects.get(pk=invoice.pk)
        payment = InvoicePayment.objects.get(pk=payment.pk)
        self.assertEqual(invoice.is_exported, 'no')
        self.assertFalse(payment.is_exported)

    def get_blank_invoice(self, inv_is_exported='no',
                          inv_is_credit_note=False, inv_invoice_related=None):
        """
        Create a blank invoice
        """
        company = Company(name="MyCompany",
                            street="rue de nantes",
                            postal_code="44105", city="NANTES Cedex 4")
        company.save()
        self.Company = company
        invoice = Invoice(recipient=self.company,
                          invoice_date=date.today(),
                          is_exported=inv_is_exported,
                          is_credit_note=inv_is_credit_note,
                          invoice_related=inv_invoice_related)
        invoice.save()
        return invoice
