# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BankAccount'
        db.create_table('bank_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('swift_bic', self.gf('django_iban.fields.SWIFTBICField')(max_length=11)),
            ('iban', self.gf('django_iban.fields.IBANField')(max_length=34)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['currencies.Currency'])),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'pyfreebill', ['BankAccount'])

        # Deleting field 'PyfbSettings.account2_currency'
        db.delete_column('pyfbsettings', 'account2_currency_id')

        # Deleting field 'PyfbSettings.account1_swift_bic'
        db.delete_column('pyfbsettings', 'account1_swift_bic')

        # Deleting field 'PyfbSettings.account2_swift_bic'
        db.delete_column('pyfbsettings', 'account2_swift_bic')

        # Deleting field 'PyfbSettings.account3_iban'
        db.delete_column('pyfbsettings', 'account3_iban')

        # Deleting field 'PyfbSettings.account3_currency'
        db.delete_column('pyfbsettings', 'account3_currency_id')

        # Deleting field 'PyfbSettings.account1_iban'
        db.delete_column('pyfbsettings', 'account1_iban')

        # Deleting field 'PyfbSettings.account3_swift_bic'
        db.delete_column('pyfbsettings', 'account3_swift_bic')

        # Deleting field 'PyfbSettings.account3'
        db.delete_column('pyfbsettings', 'account3')

        # Deleting field 'PyfbSettings.account2'
        db.delete_column('pyfbsettings', 'account2')

        # Deleting field 'PyfbSettings.account1'
        db.delete_column('pyfbsettings', 'account1')

        # Deleting field 'PyfbSettings.account1_currency'
        db.delete_column('pyfbsettings', 'account1_currency_id')

        # Deleting field 'PyfbSettings.account2_iban'
        db.delete_column('pyfbsettings', 'account2_iban')


    def backwards(self, orm):
        # Deleting model 'BankAccount'
        db.delete_table('bank_account')

        # Adding field 'PyfbSettings.account2_currency'
        db.add_column('pyfbsettings', 'account2_currency',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='account2_currency', null=True, to=orm['currencies.Currency'], blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account1_swift_bic'
        db.add_column('pyfbsettings', 'account1_swift_bic',
                      self.gf('django_iban.fields.SWIFTBICField')(max_length=11, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account2_swift_bic'
        db.add_column('pyfbsettings', 'account2_swift_bic',
                      self.gf('django_iban.fields.SWIFTBICField')(max_length=11, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account3_iban'
        db.add_column('pyfbsettings', 'account3_iban',
                      self.gf('django_iban.fields.IBANField')(max_length=34, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account3_currency'
        db.add_column('pyfbsettings', 'account3_currency',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='account3_currency', null=True, to=orm['currencies.Currency'], blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account1_iban'
        db.add_column('pyfbsettings', 'account1_iban',
                      self.gf('django_iban.fields.IBANField')(max_length=34, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account3_swift_bic'
        db.add_column('pyfbsettings', 'account3_swift_bic',
                      self.gf('django_iban.fields.SWIFTBICField')(max_length=11, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account3'
        db.add_column('pyfbsettings', 'account3',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account2'
        db.add_column('pyfbsettings', 'account2',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account1'
        db.add_column('pyfbsettings', 'account1',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account1_currency'
        db.add_column('pyfbsettings', 'account1_currency',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='account1_currency', null=True, to=orm['currencies.Currency'], blank=True),
                      keep_default=False)

        # Adding field 'PyfbSettings.account2_iban'
        db.add_column('pyfbsettings', 'account2_iban',
                      self.gf('django_iban.fields.IBANField')(max_length=34, null=True, blank=True),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'currencies.currency': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_base': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'pyfreebill.acllists': {
            'Meta': {'ordering': "('acl_name',)", 'object_name': 'AclLists', 'db_table': "'acl_lists'"},
            'acl_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'default_policy': ('django.db.models.fields.CharField', [], {'default': "'deny'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pyfreebill.aclnodes': {
            'Meta': {'ordering': "('company', 'policy', 'cidr')", 'object_name': 'AclNodes', 'db_table': "'acl_nodes'"},
            'acllist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.AclLists']"}),
            'cidr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'policy': ('django.db.models.fields.CharField', [], {'default': "'allow'", 'max_length': '10'})
        },
        u'pyfreebill.bankaccount': {
            'Meta': {'object_name': 'BankAccount', 'db_table': "'bank_account'"},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['currencies.Currency']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'iban': ('django_iban.fields.IBANField', [], {'max_length': '34'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'swift_bic': ('django_iban.fields.SWIFTBICField', [], {'max_length': '11'})
        },
        u'pyfreebill.calleridprefix': {
            'Meta': {'ordering': "('calleridprefixlist', 'prefix')", 'unique_together': "(('calleridprefixlist', 'prefix'),)", 'object_name': 'CalleridPrefix', 'db_table': "'caller_id_prefix'"},
            'calleridprefixlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.CalleridPrefixList']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'})
        },
        u'pyfreebill.calleridprefixlist': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CalleridPrefixList', 'db_table': "'callerid_prefix_list'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'pyfreebill.carriercidnormalizationrules': {
            'Meta': {'ordering': "('company',)", 'object_name': 'CarrierCIDNormalizationRules', 'db_table': "'carrier_cid_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.carriernormalizationrules': {
            'Meta': {'ordering': "('company', 'prefix')", 'object_name': 'CarrierNormalizationRules', 'db_table': "'carrier_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.cdr': {
            'Meta': {'ordering': "('start_stamp', 'customer')", 'object_name': 'CDR', 'db_table': "'cdr'"},
            'answered_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'billsec': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'bleg_uuid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'block_min_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'caller_id_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'chan_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'cost_destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cost_rate': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customer_related'", 'null': 'True', 'to': u"orm['pyfreebill.Company']"}),
            'customer_ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'destination_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'effectiv_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'effective_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'end_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'gateway': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.SofiaGateway']", 'null': 'True'}),
            'hangup_cause': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'hangup_cause_q850': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hangup_disposition': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_block': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'lcr_carrier_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carrier_related'", 'null': 'True', 'to': u"orm['pyfreebill.Company']"}),
            'lcr_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.LCRGroup']", 'null': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'ratecard_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.RateCard']", 'null': 'True'}),
            'read_codec': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'sell_destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'sip_hangup_cause': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'sip_rtp_rxstat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'sip_rtp_txstat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'sip_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'start_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'switch_ipv4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'switchname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'total_sell': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '11', 'decimal_places': '5'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'write_codec': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        u'pyfreebill.company': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Company', 'db_table': "'company'"},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'account_blocked_alert_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'account_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'billing_cycle': ('django.db.models.fields.CharField', [], {'default': "'m'", 'max_length': '10'}),
            'calls_per_second': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'cb_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['currencies.Currency']"}),
            'credit_limit': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '4'}),
            'customer_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '6'}),
            'customer_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_alert': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'iban': ('django_iban.fields.IBANField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_credit_alert': ('django.db.models.fields.DecimalField', [], {'default': "'10'", 'max_digits': '12', 'decimal_places': '4'}),
            'low_credit_alert_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_calls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'prepaid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'supplier_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '6'}),
            'supplier_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'swift_bic': ('django_iban.fields.SWIFTBICField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'vat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vat_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'vat_number_validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'pyfreebill.companybalancehistory': {
            'Meta': {'ordering': "('company', 'date_added')", 'object_name': 'CompanyBalanceHistory', 'db_table': "'company_balance_history'"},
            'amount_debited': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'amount_refund': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'customer_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '4'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation_type': ('django.db.models.fields.CharField', [], {'default': "'customer'", 'max_length': '10'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'supplier_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '4'})
        },
        u'pyfreebill.customercidnormalizationrules': {
            'Meta': {'ordering': "('company',)", 'object_name': 'CustomerCIDNormalizationRules', 'db_table': "'customer_cid_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.customerdirectory': {
            'Meta': {'ordering': "('company', 'name')", 'object_name': 'CustomerDirectory', 'db_table': "'customer_directory'"},
            'calls_per_second': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'cli_debug': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codecs': ('django.db.models.fields.CharField', [], {'default': "'ALL'", 'max_length': '100'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fake_ring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignore_early_media': ('django.db.models.fields.CharField', [], {'default': "'false'", 'max_length': '20'}),
            'log_auth_failures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_calls': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'multiple_registrations': ('django.db.models.fields.CharField', [], {'default': "'false'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'outbound_caller_id_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'outbound_caller_id_number': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'registration': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rtp_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'sip_ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sip_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5060'}),
            'vmd': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'pyfreebill.customernormalizationrules': {
            'Meta': {'ordering': "('company', 'prefix')", 'object_name': 'CustomerNormalizationRules', 'db_table': "'customer_norm_rules'"},
            'add_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remove_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.customerratecards': {
            'Meta': {'ordering': "('company', 'priority', 'ratecard')", 'object_name': 'CustomerRateCards', 'db_table': "'customer_ratecards'"},
            'allow_negative_margin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'ratecard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.RateCard']"}),
            'tech_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7', 'null': 'True', 'blank': 'True'})
        },
        u'pyfreebill.customerrates': {
            'Meta': {'ordering': "('ratecard', 'prefix', 'enabled')", 'unique_together': "(('ratecard', 'prefix'),)", 'object_name': 'CustomerRates', 'db_table': "'customer_rates'"},
            'block_min_duration': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_block': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '5'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '5'}),
            'ratecard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.RateCard']"})
        },
        u'pyfreebill.destinationnumberrules': {
            'Meta': {'ordering': "('prefix',)", 'object_name': 'DestinationNumberRules', 'db_table': "'destination_norm_rules'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'format_num': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'pyfreebill.dimcustomerdestination': {
            'Meta': {'ordering': "('date', 'customer', 'destination')", 'object_name': 'DimCustomerDestination', 'db_table': "'dim_customer_destination'"},
            'avg_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'success_calls': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'total_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_sell': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'pyfreebill.dimcustomerhangupcause': {
            'Meta': {'ordering': "('date', 'customer', 'hangupcause')", 'object_name': 'DimCustomerHangupcause', 'db_table': "'dim_customer_hangupcause'"},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.dimcustomersiphangupcause': {
            'Meta': {'ordering': "('date', 'customer', 'sip_hangupcause')", 'object_name': 'DimCustomerSipHangupcause', 'db_table': "'dim_customer_sip_hangupcause'"},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sip_hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.dimdate': {
            'Meta': {'ordering': "('date',)", 'object_name': 'DimDate', 'db_table': "'date_dimension'"},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'day_of_week': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hour': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'pyfreebill.dimproviderdestination': {
            'Meta': {'ordering': "('date', 'provider', 'destination')", 'object_name': 'DimProviderDestination', 'db_table': "'dim_provider_destination'"},
            'avg_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'success_calls': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'total_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_sell': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'pyfreebill.dimproviderhangupcause': {
            'Meta': {'ordering': "('date', 'provider', 'hangupcause')", 'object_name': 'DimProviderHangupcause', 'db_table': "'dim_provider_hangupcause'"},
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.dimprovidersiphangupcause': {
            'Meta': {'ordering': "('date', 'provider', 'sip_hangupcause')", 'object_name': 'DimProviderSipHangupcause', 'db_table': "'dim_provider_sip_hangupcause'"},
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.DimDate']"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'sip_hangupcause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'total_calls': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pyfreebill.emailaddress': {
            'Meta': {'object_name': 'EmailAddress', 'db_table': "'contacts_email_addresses'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        u'pyfreebill.group': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Group', 'db_table': "'contacts_groups'"},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'companies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pyfreebill.Company']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pyfreebill.Person']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'pyfreebill.hangupcause': {
            'Meta': {'ordering': "('code',)", 'object_name': 'HangupCause', 'db_table': "'hangup_cause'"},
            'cause': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enumeration': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pyfreebill.instantmessenger': {
            'Meta': {'object_name': 'InstantMessenger', 'db_table': "'contacts_instant_messengers'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'im_account': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'default': "'jabber'", 'max_length': '11'})
        },
        u'pyfreebill.lcrgroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'LCRGroup', 'db_table': "'lcr_group'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcrtype': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'pyfreebill.lcrproviders': {
            'Meta': {'object_name': 'LCRProviders', 'db_table': "'lcr_providers'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.LCRGroup']"}),
            'provider_tariff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.ProviderTariff']"})
        },
        u'pyfreebill.person': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'Person', 'db_table': "'contacts_people'"},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'pyfreebill.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber', 'db_table': "'contacts_phone_numbers'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'pyfreebill.providerrates': {
            'Meta': {'ordering': "('enabled', 'provider_tariff', 'digits')", 'unique_together': "(('digits', 'provider_tariff'),)", 'object_name': 'ProviderRates', 'db_table': "'provider_rates'", 'index_together': "[['provider_tariff', 'digits', 'enabled']]"},
            'block_min_duration': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'cost_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '5'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'destination': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'digits': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_block': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '5'}),
            'provider_tariff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.ProviderTariff']"})
        },
        u'pyfreebill.providertariff': {
            'Meta': {'ordering': "('enabled', 'quality', 'reliability')", 'object_name': 'ProviderTariff', 'db_table': "'provider_tariff'"},
            'callerid_filter': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '2'}),
            'callerid_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.CalleridPrefixList']", 'null': 'True', 'blank': 'True'}),
            'carrier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'cid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['currencies.Currency']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_strip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'default': "'100'", 'blank': 'True'}),
            'reliability': ('django.db.models.fields.IntegerField', [], {'default': "'100'", 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'tail_strip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'})
        },
        u'pyfreebill.pyfbsettings': {
            'Meta': {'object_name': 'PyfbSettings', 'db_table': "'pyfbsettings'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'default_currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_currency'", 'null': 'True', 'to': u"orm['currencies.Currency']"}),
            'home_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'vat_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'pyfreebill.ratecard': {
            'Meta': {'ordering': "('name', 'enabled')", 'object_name': 'RateCard', 'db_table': "'ratecard'"},
            'callerid_filter': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '2'}),
            'callerid_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.CalleridPrefixList']", 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['currencies.Currency']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lcrgroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.LCRGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'pyfreebill.services': {
            'Meta': {'object_name': 'Services', 'db_table': "'services'"},
            'account_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['currencies.Currency']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'default': "'monthly'", 'max_length': '100'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'tax1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tax1'", 'null': 'True', 'to': u"orm['pyfreebill.Taxes']"}),
            'tax2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tax2'", 'null': 'True', 'to': u"orm['pyfreebill.Taxes']"}),
            'type_service': ('django.db.models.fields.CharField', [], {'default': "'periodic'", 'max_length': '100'}),
            'unit_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'vat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vatservices'", 'to': u"orm['pyfreebill.Taxes']"})
        },
        u'pyfreebill.sipprofile': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('sip_ip', 'sip_port'),)", 'object_name': 'SipProfile', 'db_table': "'sip_profile'"},
            'NDLB_broken_auth_hash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'NDLB_force_rport': ('django.db.models.fields.CharField', [], {'default': "'Null'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'NDLB_rec_in_nat_reg_c': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'accept_blind_reg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aggressive_nat_detection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apply_inbound_acl': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'auth_calls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'disable_register': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'disable_transcoding': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'enable_timer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ext_rtp_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'ext_sip_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbound_codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,PCMA'", 'max_length': '100'}),
            'log_auth_failures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'outbound_codec_prefs': ('django.db.models.fields.CharField', [], {'default': "'G729,PCMU,PCMA'", 'max_length': '100'}),
            'pass_rfc2833': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rtp_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'rtp_rewrite_timestamps': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_timeout': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1800'}),
            'sip_ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'sip_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5060'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'default': "'pyfreebilling'", 'max_length': '50'})
        },
        u'pyfreebill.sofiagateway': {
            'Meta': {'ordering': "('company', 'name')", 'object_name': 'SofiaGateway', 'db_table': "'sofia_gateway'"},
            'caller_id_in_from': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'channels': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'codec': ('django.db.models.fields.CharField', [], {'default': "'ALL'", 'max_length': '30'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'expire_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3600', 'null': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'from_domain': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '35', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'proxy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '48'}),
            'realm': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'register': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'retry_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30', 'null': 'True'}),
            'sip_cid_type': ('django.db.models.fields.CharField', [], {'default': "'rpid'", 'max_length': '10'}),
            'sip_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyfreebill.SipProfile']"}),
            'suffix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '35', 'blank': 'True'})
        },
        u'pyfreebill.specialdate': {
            'Meta': {'object_name': 'SpecialDate', 'db_table': "'contacts_special_dates'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'every_year': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'occasion': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        },
        u'pyfreebill.streetaddress': {
            'Meta': {'object_name': 'StreetAddress', 'db_table': "'contacts_street_addresses'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'pyfreebill.subscriptions': {
            'Meta': {'object_name': 'Subscriptions', 'db_table': "'subscriptions'"},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customer'", 'to': u"orm['pyfreebill.Company']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateTimeField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['pyfreebill.Services']"})
        },
        u'pyfreebill.taxes': {
            'Meta': {'object_name': 'Taxes', 'db_table': "'taxes'"},
            'account_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '4'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'taxes': ('django.db.models.fields.CharField', [], {'default': "'False'", 'max_length': '100'})
        },
        u'pyfreebill.voipswitch': {
            'Meta': {'ordering': "('name',)", 'object_name': 'VoipSwitch', 'db_table': "'voip_switch'"},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'esl_listen_ip': ('django.db.models.fields.CharField', [], {'default': "'127.0.0.1'", 'max_length': '100'}),
            'esl_listen_port': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'8021'"}),
            'esl_password': ('django.db.models.fields.CharField', [], {'default': "'ClueCon'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'pyfreebill.website': {
            'Meta': {'object_name': 'WebSite', 'db_table': "'contacts_web_sites'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '6'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['pyfreebill']