# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Clientes.celular'
        db.delete_column(u'app1_clientes', 'celular')

        # Deleting field 'Proveedores.telefono2'
        db.delete_column(u'app1_proveedores', 'telefono2')

        # Deleting field 'Productos.precio2'
        db.delete_column(u'app1_productos', 'precio2')

        # Deleting field 'Categorias.tipodecat'
        db.delete_column(u'app1_categorias', 'tipodecat')


    def backwards(self, orm):
        # Adding field 'Clientes.celular'
        db.add_column(u'app1_clientes', 'celular',
                      self.gf('django.db.models.fields.CharField')(default=-19, max_length=50),
                      keep_default=False)

        # Adding field 'Proveedores.telefono2'
        db.add_column(u'app1_proveedores', 'telefono2',
                      self.gf('django.db.models.fields.CharField')(default=55, max_length=50),
                      keep_default=False)

        # Adding field 'Productos.precio2'
        db.add_column(u'app1_productos', 'precio2',
                      self.gf('django.db.models.fields.FloatField')(default=10),
                      keep_default=False)

        # Adding field 'Categorias.tipodecat'
        db.add_column(u'app1_categorias', 'tipodecat',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=50),
                      keep_default=False)


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
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'app1.proveedores': {
            'Meta': {'object_name': 'Proveedores'},
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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