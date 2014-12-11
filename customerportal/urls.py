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

from django.conf.urls import patterns, include, url

from customerportal.views import ContactUsCustView, NotificationsUpdateCustView, HomePageCustView, ProfileCustView, BalanceHistoryCustView, CdrReportCustView, SipAccountCustView, csv_view, ListExportCustView


urlpatterns = patterns('',
                       url(r'^$', HomePageCustView.as_view(), name='home'),
                       url(r'^sip_account/$', SipAccountCustView.as_view(), name='sip_account'),
                       url(r'^balance/$', BalanceHistoryCustView.as_view(), name='balance_history'),
                       url(r'^stats/$', CdrReportCustView.as_view(), name='stats'),
                       url(r'^reports/$', ListExportCustView.as_view(), name='list_export'),
                       url(r'^notifications/(?P<pk>\d+)/$', NotificationsUpdateCustView.as_view(), name='notifications_update'),
                       url(r'^cdr_export/(?P<month>\d{1})/(?P<day>\d{1})/$', 'customerportal.views.csv_view', name='report'),
                       url(r'^cdr_report/$', CdrReportCustView.as_view(), name='cdr_report'),
                       url(r'^contact_us/$', ContactUsCustView.as_view(), name='contact_us'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'customer/login.html'}),
                       url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change',
                           {'template_name': 'customer/password_change_form.html'}),
                       url(r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done',
                           {'template_name': 'customer/password_change_done.html'},
                           name='password_change_done'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
                       url(r'^accounts/profile/$', ProfileCustView.as_view(), name='user_profile'), )