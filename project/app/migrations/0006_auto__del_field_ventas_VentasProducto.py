# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ventas.VentasProducto'
        db.delete_column(u'app_ventas', 'VentasProducto_id')

        # Adding M2M table for field VentasProducto on 'Ventas'
        m2m_table_name = db.shorten_name(u'app_ventas_VentasProducto')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ventas', models.ForeignKey(orm[u'app.ventas'], null=False)),
            ('ventasproducto', models.ForeignKey(orm[u'app.ventasproducto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ventas_id', 'ventasproducto_id'])


    def backwards(self, orm):
        # Adding field 'Ventas.VentasProducto'
        db.add_column(u'app_ventas', 'VentasProducto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=5, to=orm['app.VentasProducto']),
                      keep_default=False)

        # Removing M2M table for field VentasProducto on 'Ventas'
        db.delete_table(db.shorten_name(u'app_ventas_VentasProducto'))


    models = {
        u'app.categorias': {
            'Meta': {'object_name': 'Categorias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.clientes': {
            'Meta': {'object_name': 'Clientes'},
            'a_materno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'a_paterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'app.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'comentario': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.materia_prima': {
            'Meta': {'object_name': 'Materia_Prima'},
            'costo': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Proveedores']"}),
            'unidad_presentacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Unidades_Presentacion']"})
        },
        u'app.productos': {
            'Meta': {'object_name': 'Productos'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Categorias']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.proveedores': {
            'Meta': {'object_name': 'Proveedores'},
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'ejemplo@mail.com'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Productos']", 'symmetrical': 'False'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "'55-'", 'max_length': '50'})
        },
        u'app.recetas': {
            'Meta': {'object_name': 'Recetas'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_prima': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Materia_Prima']", 'symmetrical': 'False'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Productos']"}),
            'unidad_de_medida': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.unidades_presentacion': {
            'Meta': {'object_name': 'Unidades_Presentacion'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'administrador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'perfil': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'usuario': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35', 'db_index': 'True'})
        },
        u'app.ventas': {
            'Meta': {'object_name': 'Ventas'},
            'VentasProducto': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.VentasProducto']", 'symmetrical': 'False'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Clientes']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.FloatField', [], {}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'totalcantidad': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.ventasproducto': {
            'Meta': {'object_name': 'VentasProducto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'claveproducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Productos']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']