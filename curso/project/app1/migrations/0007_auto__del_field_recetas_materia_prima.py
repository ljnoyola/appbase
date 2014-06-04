# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recetas.materia_prima'
        db.delete_column(u'app1_recetas', 'materia_prima_id')

        # Adding M2M table for field materia_prima on 'Recetas'
        m2m_table_name = db.shorten_name(u'app1_recetas_materia_prima')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recetas', models.ForeignKey(orm[u'app1.recetas'], null=False)),
            ('materia_prima', models.ForeignKey(orm[u'app1.materia_prima'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recetas_id', 'materia_prima_id'])


    def backwards(self, orm):
        # Adding field 'Recetas.materia_prima'
        db.add_column(u'app1_recetas', 'materia_prima',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=5, to=orm['app1.Materia_Prima']),
                      keep_default=False)

        # Removing M2M table for field materia_prima on 'Recetas'
        db.delete_table(db.shorten_name(u'app1_recetas_materia_prima'))


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
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app1.Productos']", 'symmetrical': 'False'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'55-'", 'max_length': '50'})
        },
        u'app1.recetas': {
            'Meta': {'object_name': 'Recetas'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_prima': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app1.Materia_Prima']", 'symmetrical': 'False'}),
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