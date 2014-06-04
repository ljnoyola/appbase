# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorias'
        db.create_table(u'app1_categorias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipodecat', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app1', ['Categorias'])

        # Adding model 'Productos'
        db.create_table(u'app1_productos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Categorias'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app1', ['Productos'])

        # Adding model 'Proveedores'
        db.create_table(u'app1_proveedores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app1', ['Proveedores'])

        # Adding model 'Unidades_Presentacion'
        db.create_table(u'app1_unidades_presentacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app1', ['Unidades_Presentacion'])

        # Adding model 'Materia_Prima'
        db.create_table(u'app1_materia_prima', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('costo', self.gf('django.db.models.fields.FloatField')()),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Proveedores'])),
            ('unidad_presentacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Unidades_Presentacion'])),
        ))
        db.send_create_signal(u'app1', ['Materia_Prima'])

        # Adding model 'Clientes'
        db.create_table(u'app1_clientes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('a_paterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('a_materno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app1', ['Clientes'])

        # Adding model 'Ventas'
        db.create_table(u'app1_ventas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Clientes'])),
            ('subtotal', self.gf('django.db.models.fields.FloatField')()),
            ('iva', self.gf('django.db.models.fields.FloatField')()),
            ('totalcantidad', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app1', ['Ventas'])

        # Adding model 'Recetas'
        db.create_table(u'app1_recetas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Productos'])),
            ('materia_prima', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Materia_Prima'])),
            ('unidad_de_medida', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app1', ['Recetas'])


    def backwards(self, orm):
        # Deleting model 'Categorias'
        db.delete_table(u'app1_categorias')

        # Deleting model 'Productos'
        db.delete_table(u'app1_productos')

        # Deleting model 'Proveedores'
        db.delete_table(u'app1_proveedores')

        # Deleting model 'Unidades_Presentacion'
        db.delete_table(u'app1_unidades_presentacion')

        # Deleting model 'Materia_Prima'
        db.delete_table(u'app1_materia_prima')

        # Deleting model 'Clientes'
        db.delete_table(u'app1_clientes')

        # Deleting model 'Ventas'
        db.delete_table(u'app1_ventas')

        # Deleting model 'Recetas'
        db.delete_table(u'app1_recetas')


    models = {
        u'app1.categorias': {
            'Meta': {'object_name': 'Categorias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipodecat': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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