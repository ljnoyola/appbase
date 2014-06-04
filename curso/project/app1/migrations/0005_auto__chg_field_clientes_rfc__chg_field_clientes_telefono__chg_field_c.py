# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Clientes.rfc'
        db.alter_column(u'app1_clientes', 'rfc', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Clientes.telefono'
        db.alter_column(u'app1_clientes', 'telefono', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Clientes.email'
        db.alter_column(u'app1_clientes', 'email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Proveedores.rfc'
        db.alter_column(u'app1_proveedores', 'rfc', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Productos.descripcion'
        db.alter_column(u'app1_productos', 'descripcion', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Clientes.rfc'
        db.alter_column(u'app1_clientes', 'rfc', self.gf('django.db.models.fields.CharField')(default=123, max_length=50))

        # Changing field 'Clientes.telefono'
        db.alter_column(u'app1_clientes', 'telefono', self.gf('django.db.models.fields.CharField')(default=456, max_length=50))

        # Changing field 'Clientes.email'
        db.alter_column(u'app1_clientes', 'email', self.gf('django.db.models.fields.CharField')(default=55, max_length=50))

        # Changing field 'Proveedores.rfc'
        db.alter_column(u'app1_proveedores', 'rfc', self.gf('django.db.models.fields.CharField')(default=45, max_length=50))

        # Changing field 'Productos.descripcion'
        db.alter_column(u'app1_productos', 'descripcion', self.gf('django.db.models.fields.TextField')(default=5))

    models = {
        u'app1.categorias': {
            'Meta': {'object_name': 'Categorias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app1.clientes': {
            'Meta': {'object_name': 'Clientes'},
            'a_materno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'a_paterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'app1.materia_prima': {
            'Meta': {'object_name': 'Materia_Prima'},
            'costo': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app1.Proveedores']"}),
            'unidad_presentacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app1.Unidades_Presentacion']"})
        },
        u'app1.productos': {
            'Meta': {'object_name': 'Productos'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app1.Categorias']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'app1.proveedores': {
            'Meta': {'object_name': 'Proveedores'},
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'ejemplo@mail.com'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'55-'", 'max_length': '50'})
        },
        u'app1.recetas': {
            'Meta': {'object_name': 'Recetas'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_prima': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app1.Materia_Prima']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app1.Productos']"}),
            'unidad_de_medida': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app1.unidades_presentacion': {
            'Meta': {'object_name': 'Unidades_Presentacion'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app1.ventas': {
            'Meta': {'object_name': 'Ventas'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app1.Clientes']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.FloatField', [], {}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'totalcantidad': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['app1']