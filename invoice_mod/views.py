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

import csv
import datetime

from django.http import HttpResponse

from .export import export_annuel_gather_data
from .export import InvoiceResource
from invoice.models import Invoice


def export_annuel_view(request):
    """
    Export invoice (with is_exported flag to 'yes') for current year.
    """

    filename = "export_annue.csv"
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename

    data = export_annuel_gather_data()

    writer = csv.writer(response)
    # We do this because CSV doesn't support directly Unicode and UTF-8
    # http://docs.python.org/2/library/csv.html#examples
    for row in data:
        r = []
        for field in row:
            r.append(("%s" % field).strip().encode("utf-8"))
        writer.writerow(r)

    return response


def export_factures_view(request):
    qs = Invoice.objects.filter(
        invoice_date__year=datetime.date.today().year).order_by('-invoice_date')
    data = InvoiceResource().export(qs)
    #import pdb; pdb.set_trace()

    filename = u"export_factures.xls"
    content_type = 'application/application/vnd.ms-excel'

    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename
    response.write(data.xls)
    return response