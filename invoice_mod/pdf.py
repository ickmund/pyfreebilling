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

from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.rl_config import defaultPageSize
from reportlab.lib import colors
from invoice.conf import settings
from invoice.utils import format_currency
from invoice.pdf import header_func, address_func, footer_func

PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]


def draw_header(canvas, invoice):
    """ Draws the invoice header """
    canvas.setFont('Helvetica-Bold', 14)
    if invoice.is_credit_note:
        canvas.drawCentredString(PAGE_WIDTH / 2.0, -8.5 * cm,
                                 "AVOIR SUR FACTURE %s" %
                                 invoice.invoice_related.invoice_id)
    else:
        canvas.drawCentredString(PAGE_WIDTH / 2.0, -8.5 * cm, "FACTURE")

    #canvas.drawImage(settings.INV_LOGO, 1 * cm, -5 * cm, 100, 87)
    canvas.drawImage(settings.INV_LOGO, 1 * cm, -5 * cm, 125, 109)


def draw_address(canvas):
    """ Draws the business address """
    canvas.setLineWidth(0.5)
    canvas.rect(12 * cm, -4 * cm, 6 * cm, 2 * cm, )

    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(15 * cm, -2.5 * cm, "SERVICE EMETTEUR")
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawCentredString(15 * cm, -2.8 * cm, "company")
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawCentredString(15 * cm, -3.1 * cm, "adresse 1")
    canvas.drawCentredString(15 * cm, -3.4 * cm, "adresse 2")
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(15 * cm, -3.7 * cm, "CP VILLE")


def draw_footer(canvas):
    """ Draws the invoice footer """
    pass


def draw_pdf(buffer, invoice):
    """ Draws the invoice """
    canvas = Canvas(buffer, pagesize=A4)
    canvas.translate(0, 29.7 * cm)
    canvas.setFont('Helvetica', 10)

    canvas.saveState()
    header_func(canvas, invoice)
    canvas.restoreState()

    canvas.saveState()
    footer_func(canvas)
    canvas.restoreState()

    canvas.saveState()
    address_func(canvas)
    canvas.restoreState()

    # Client address
    textobject = canvas.beginText(12 * cm, -5 * cm)
    if invoice.recipient.name:
        textobject.textLine(invoice.recipient.invoice_name)
    textobject.textLine("Service de la comptabilité")
    if invoice.recipient.invoice_street:
        textobject.textLine(invoice.recipient.invoice_street)
    if invoice.recipient.invoice_complement_1:
        textobject.textLine(invoice.recipient.invoice_complement_1)
    if invoice.recipient.invoice_complement_2:
        textobject.textLine(invoice.recipient.invoice_complement_2)
    if invoice.recipient.invoice_postcode and invoice.recipient.invoice_town:
        textobject.textLine(invoice.recipient.invoice_postcode + " " +
                            invoice.recipient.invoice_town.upper())
    elif invoice.recipient.invoice_town:
        textobject.textLine(invoice.recipient.invoice_town)

    canvas.setFont('Helvetica', 10)
    canvas.drawText(textobject)

    # Info
    textobject = canvas.beginText(1 * cm, -8.5 * cm)
    if invoice.recipient.main_contact:
        textobject.textLine(u'Contact : %s %s' % (
            invoice.recipient.main_contact.firstname,
            invoice.recipient.main_contact.lastname.upper()))
    textobject.textLine(u'N° Facture : %s' % invoice.invoice_id)
    textobject.textLine(u'N° Client : %s' % invoice.recipient.client_code)
    canvas.setFont('Helvetica', 8)
    canvas.drawText(textobject)

    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawCentredString(PAGE_WIDTH / 2.0, -9 * cm,
                             u'Fait à Nantes, le %s' %
                             invoice.invoice_date.strftime('%d/%m/%Y'))

    # Items
    data = [[u'LIBELLE',
             u'QUANTITE',
             u'PRIX UNITAIRE en €',
             u'MONTANT HT en €'], ]
    for item in invoice.items.all():
        data.append([
            item.description,
            item.quantity,
            format_currency(item.unit_price),
            format_currency(item.total())
        ])
    for x in range(0, 10 - len(invoice.items.all())):
        data.append([
            u'',
            u'',
            u'',
            u'',
        ])
    payments = invoice.payments.all()
    PAYMENT_METHOD = {'cheque': u'Chèque', 'virement': u'Virement'}
    if invoice.is_paid and payments.count() >= 1:
        str_payment_method = u""
        str_payment_info = u""
        for payment in payments:
            if payment.method in PAYMENT_METHOD:
                str_payment_method += u"%s, " % PAYMENT_METHOD[payment.method]
            else:
                str_payment_method += u"%s, " % payment.method
            str_payment_info += u"%s, " % payment.additional_info

        str_payment_method = str_payment_method.rstrip(', ')
        str_payment_info = str_payment_info.rstrip(', ')
        data.append([u'Réglé par : %s' % str_payment_method, u'',
                     u'Total H.T. :', format_currency(invoice.total())])
        data.append([u'%s' % str_payment_info, u'', u'Total T.V.A. :',
                     u'Sans TVA'])
        data.append([u'Le : %s' % payment.paid_date.strftime('%d/%m/%Y'), u'',
                     u'Total T.T.C. :', format_currency(invoice.total())])
    else:
        data.append([u'Réglé par : ', u'', u'Total H.T. :',
                     format_currency(invoice.total())])
        data.append([u'', u'', u'Total T.V.A. :', u'Sans TVA'])
        data.append([u'Le : ', u'', u'Total T.T.C. :',
                     format_currency(invoice.total())])
    if invoice.is_paid and invoice.last_payment() and not invoice.is_credit_note:
        data.append([u"TVA :  association loi 1901 sans but lucratif, non "
                     u"soumise à TVA en application de l'article 261-7-1° du "
                     u"CGI ", u'', 'NET ACQUITTE',
                     format_currency(invoice.total())])
    else:
        data.append([u"TVA :  association loi 1901 sans but lucratif, non "
                     u"soumise à TVA en application de l'article 261-7-1° du "
                     u"CGI ", u'', 'NET A PAYER',
                     format_currency(invoice.total())])
    table = Table(data, colWidths=[10 * cm, 2 * cm, 3.5 * cm, 3.5 * cm])
    table.setStyle([
        ('FONT', (0, 0), (3, 0), 'Helvetica-Bold'),
        ('FONT', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        # Top grid
        ('GRID', (0, 0), (-1, 0), 0.5, colors.black),
        ('ALIGN', (0, 0), (3, 0), 'CENTER'),
        # Total grid
        ('GRID', (2, 11), (-1, 14), 0.5, colors.black),
        ('ALIGN', (-1, 11), (-1, 14), 'CENTER'),
        ('ALIGN', (2, 11), (2, 14), 'RIGHT'),
        ('FONT', (2, -11), (-1, 14), 'Helvetica-Bold'),
        ('BACKGROUND', (-1, -1), (-1, -1), (0.85, 0.85, 0.85)),
        # 'Libellé' box
        ('BOX', (0, 1), (0, 10), 0.5, colors.black),
        # 'P.U.' box
        ('BOX', (2, 1), (2, 10), 0.5, colors.black),
        # 'Montant' box
        ('BOX', (3, 1), (3, 10), 0.5, colors.black),
        # 'Paiment' box
        ('BOX', (0, 11), (1, 13), 0.5, colors.black),
        # 'TVA texte' box
        ('BOX', (0, 14), (1, 14), 0.5, colors.black),
        ('FONTSIZE', (0, 14), (1, 14), 7),
    ])
    tw, th, = table.wrapOn(canvas, 15 * cm, 19 * cm)
    table.drawOn(canvas, 1 * cm, -9.5 * cm - th)

    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(PAGE_WIDTH / 2.0, -19.5 * cm,
                             "company – N° Siret : ")

    # If the invoice have a credit note we still displaying this part
    if (not invoice.is_credit_note) and (not invoice.last_payment()):

        canvas.setDash(6, 3)
        canvas.setLineWidth(0.5)
        canvas.setFillColor((0.85, 0.85, 0.85))
        canvas.rect(6 * cm, -26 * cm, 14 * cm, 6 * cm, fill=1)
        canvas.setFillColor(colors.black)
        canvas.setDash(6, 0)

        canvas.setFont('Helvetica', 7)
        canvas.drawString(9 * cm, -20.5 * cm, "Papillon détachable")
        canvas.setFont('Helvetica-Bold', 7)
        canvas.drawString(13 * cm, -20.5 * cm,
                          "Papillon à joindre à votre règlement")

        canvas.setFont('Helvetica-Bold', 7)
        canvas.drawString(6.5 * cm, -21.5 * cm, "Date FACTURE")
        canvas.drawString(6.5 * cm, -21.8 * cm, "N° DE FACTURE")
        canvas.setFont('Helvetica', 7)
        canvas.drawString(8.3 * cm, -21.5 * cm, " : %s" %
                          invoice.invoice_date.strftime('%d/%m/%Y'))
        canvas.drawString(8.5 * cm, -21.8 * cm, " : %s" % invoice.invoice_id)

        canvas.setFont('Helvetica', 7)
        if invoice.recipient.name:
            canvas.drawString(14 * cm, -21.5 * cm, "%s" %
                              invoice.recipient.name)
        canvas.setFont('Helvetica-Bold', 7)
        canvas.drawString(14 * cm, -21.8 * cm, "N° CLIENT")
        canvas.setFont('Helvetica', 7)
        canvas.drawString(15.3 * cm, -21.8 * cm, " : %s" %
                          invoice.recipient.client_code)

        canvas.setFont('Helvetica-Bold', 10)
        canvas.drawString(10 * cm, -23 * cm, "NET A PAYER")

        canvas.setFont('Helvetica-Bold', 10)
        canvas.drawString(14 * cm, -23 * cm, "%s" %
                          format_currency(item.total()))
        canvas.setLineWidth(1.5)
        canvas.rect(13.5 * cm, -23.3 * cm, 3.8 * cm, 1 * cm)

        canvas.setLineWidth(0.5)
        canvas.rect(8 * cm, -26 * cm, 5 * cm, 2 * cm)
        canvas.setFont('Helvetica', 7)
        canvas.drawString(8.1 * cm, -24.3 * cm, "LIBELLER")
        canvas.drawString(8.1 * cm, -24.7 * cm, "Le chèque à :")
        canvas.drawString(8.1 * cm, -25 * cm, "ou virement à :")
        canvas.drawString(8.1 * cm, -25.6 * cm,
                          "(Merci de rappeler les N° de Facture et de")
        canvas.drawString(8.1 * cm, -25.9 * cm, "Client)")
        canvas.setFont('Helvetica-Bold', 7)
        canvas.drawString(9.7 * cm, -24.7 * cm, "company")
        canvas.drawString(9.8 * cm, -25 * cm, "bank number")
        canvas.drawString(8.1 * cm, -25.3 * cm, "account number")

        canvas.rect(13 * cm, -26 * cm, 5 * cm, 2 * cm)
        canvas.setFont('Helvetica', 7)
        canvas.drawString(13.1 * cm, -24.3 * cm, "ADRESSER à :")
        canvas.setFont('Helvetica-Bold', 7)
        canvas.drawString(13.1 * cm, -24.7 * cm, "company")
        canvas.drawString(13.1 * cm, -25 * cm, "rue")
        canvas.drawString(13.1 * cm, -25.3 * cm, "BP ville")
        canvas.drawString(13.1 * cm, -25.6 * cm, "email")
        canvas.drawString(13.1 * cm, -25.9 * cm, "Tél : 0xxxxxx")

        canvas.setFont('Helvetica', 6)
        textobject = canvas.beginText(1 * cm, -27 * cm)


        textobject.textLine("PENALITES : En cas de défaut de règlement dans les "
                            "60 jours suivant la date d'émission de la présente "
                            "facture, il sera appliqué à l'intégralité des sommes "
                            "en cause de plein droit et sans aucune mise ")
        textobject.textLine("en demeure "
                            "préalable, un intérêt de retard équivalent à 1,5 "
                            "fois le taux d'intérêt légal.")
        textobject.textLine("Une indemnité forfaitaire pour frais de recouvrement "
                            "de 40€ s’ajoutera à ces pénalités de retard, si les "
                            "frais de recouvrement sont supérieurs à 40 €, une "
                            "indemnisation complémentaire sera demandée ")
        textobject.textLine("sur justificatifs.")
        canvas.drawText(textobject)

    canvas.showPage()
    canvas.save()
    return canvas
