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

from django.contrib import admin
from django.conf.urls import patterns, url
from django import forms
from invoice.models import Invoice, InvoiceItem, InvoicePayment
from invoice.views import pdf_dl_view, pdf_gen_view
from invoice.forms import InvoiceAdminForm
from invoice.admin_actions import generate_credit_note

from .views import export_annuel_view, export_factures_view
from .admin_actions import send_invoice, compile_all_pdf


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem

    def __init__(self, *args, **kwargs):
        super(InvoiceItemForm, self).__init__(*args, **kwargs)
        # Because of our PDF template
        self.fields['description'].widget.attrs['maxlength'] = "60"


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    # because of invoice_mod.pdf, it does not support multiple pages yet
    max_num = 10
    fields = ('description', 'unit_price', 'quantity', )
    form = InvoiceItemForm


class InvoicePaymentInline(admin.TabularInline):
    model = InvoicePayment


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline, InvoicePaymentInline, ]
    fieldsets = [
        (None, {
            'fields': ['recipient', 'invoice_date',
                       'invoice_cost_code']
        }),
        ('Avoir', {
            'classes': ('collapse', ),
            'fields': ['is_credit_note', 'credit_note_related_link',
                       'invoice_related_link']
        })
    ]

    readonly_fields = ['credit_note_related_link', 'is_credit_note',
                       'invoice_related_link', ]

    def get_readonly_fields(self, request, obj=None):
        if hasattr(obj, 'is_exported'):
            if obj.is_exported in ('invoice_only', 'yes'):
                return ['credit_note_related_link', 'is_credit_note',
                        'invoice_related_link', 'recipient', 'invoice_date',
                        'invoice_cost_code']
        return ['credit_note_related_link', 'is_credit_note',
                'invoice_related_link', ]

    search_fields = ('invoice_id', 'recipient__name')
    list_filter = ['invoice_date', 'invoice_cost_code', 'invoiced',
                   'is_credit_note', 'is_paid', ]
    list_display = (
        'invoice_id',
        'total_amount',
        'recipient',
        'invoice_date',
        'invoiced',
        'is_paid',
        'is_credit_note',
    )
    form = InvoiceAdminForm
    actions = [send_invoice, compile_all_pdf, generate_credit_note]

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(InvoiceAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_urls(self):
        urls = super(InvoiceAdmin, self).get_urls()
        wrapped_pdf_dl_view = self.admin_site.admin_view(pdf_dl_view)
        wrapped_pdf_gen_view = self.admin_site.admin_view(pdf_gen_view)
        wrapped_export_annuel_view = self.admin_site.admin_view(
            export_annuel_view)
        wrapped_export_factures_view = self.admin_site.admin_view(
            export_factures_view)
        urls = patterns(
            '',
            url(r'^(.+)/pdf/download/$', wrapped_pdf_dl_view),
            url(r'^(.+)/pdf/generate/$', wrapped_pdf_gen_view),
            url(r'^export_annuel/$', wrapped_export_annuel_view,
                name='export_annuel'),
            url(r'^export_factures/$', wrapped_export_factures_view,
                name='export_factures'),
        ) + urls
        return urls


admin.site.unregister(Invoice)

admin.site.register(Invoice, InvoiceAdmin)