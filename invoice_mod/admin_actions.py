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

from django.contrib import messages
from django.http import HttpResponse

from PyPDF2 import PdfFileMerger, PdfFileReader

from invoice_mod import send_relance

import logging
logger = logging.getLogger(__name__)


def send_invoice(self, request, queryset):
    count_mail_sent = 0
    for invoice in queryset.all():
        if(not invoice.is_paid):
            mail_sent = None
            try:
                mail_sent = send_relance(invoice)
                count_mail_sent += 1
                logger.info(u'Envoi facture OK! - %s ' % invoice.invoice_id)
            except:
                pass
            if not mail_sent:
                messages.add_message(
                    request, messages.ERROR, u"Un problème est survenu lors "
                    u"de l'envoi d'email! (facture en cours de traitement : "
                    u"%s)" % invoice.invoice_id)
                break
        else:
            messages.add_message(
                request, messages.ERROR, u"Il n'est pas possible d'envoyer "
                u"une relance pour: une facture payée, un avoir, ou une "
                u"facture pour laquelle un avoir a été généré. (id: %s)" %
                invoice.invoice_id)
    if count_mail_sent:
        messages.add_message(request, messages.INFO,
                             u"%s relance(s) envoyée(s)" % count_mail_sent)
send_invoice.short_description = "Relance par mail"


def compile_all_pdf(self, request, queryset):
    merger = PdfFileMerger()
    for invoice in queryset.all():
        if invoice.is_pdf_generated():
            merger.append(PdfFileReader(file(invoice.pdf_path(), 'rb')))
        else:
            messages.add_message(request, messages.INFO, u"La facture %s "
                                 u"n'est pas générée, elle ne se trouve donc "
                                 u"pas dans la compilation." %
                                 invoice.invoice_id)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; "\
                                      "filename=\"compilation_factures.pdf\""
    merger.write(response)
    return response

compile_all_pdf.short_description = "Compiler les PDF"