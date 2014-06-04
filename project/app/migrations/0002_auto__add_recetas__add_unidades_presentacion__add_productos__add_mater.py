# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recetas'
        db.create_table(u'app_recetas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Productos'])),
            ('unidad_de_medida', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['Recetas'])

        # Adding M2M table for field materia_prima on 'Recetas'
        m2m_table_name = db.shorten_name(u'app_recetas_materia_prima')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recetas', models.ForeignKey(orm[u'app.recetas'], null=False)),
            ('materia_prima', models.ForeignKey(orm[u'app.materia_prima'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recetas_id', 'materia_prima_id'])

        # Adding model 'Unidades_Presentacion'
        db.create_table(u'app_unidades_presentacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'app', ['Unidades_Presentacion'])

        # Adding model 'Productos'
        db.create_table(u'app_productos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Categorias'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Productos'])

        # Adding model 'Materia_Prima'
        db.create_table(u'app_materia_prima', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('costo', self.gf('django.db.models.fields.FloatField')()),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Proveedores'])),
            ('unidad_presentacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Unidades_Presentacion'])),
        ))
        db.send_create_signal(u'app', ['Materia_Prima'])

        # Adding model 'Clientes'
        db.create_table(u'app_clientes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('a_paterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('a_materno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Clientes'])

        # Adding model 'Ventas'
        db.create_table(u'app_ventas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Clientes'])),
            ('subtotal', self.gf('django.db.models.fields.FloatField')()),
            ('iva', self.gf('django.db.models.fields.FloatField')()),
            ('totalcantidad', self.gf('django.db.models.fields.FloatField')()),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Ventas'])

        # Adding model 'Categorias'
        db.create_table(u'app_categorias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Categorias'])

        # Adding model 'Proveedores'
        db.create_table(u'app_proveedores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rfc', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('telefono', self.gf('django.db.models.fields.CharField')(default='55-', max_length=50)),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(default='ejemplo@mail.com', max_length=50)),
        ))
        db.send_create_signal(u'app', ['Proveedores'])

        # Adding M2M table for field productos on 'Proveedores'
        m2m_table_name = db.shorten_name(u'app_proveedores_productos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proveedores', models.ForeignKey(orm[u'app.proveedores'], null=False)),
            ('productos', models.ForeignKey(orm[u'app.productos'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proveedores_id', 'productos_id'])


    def backwards(self, orm):
        # Deleting model 'Recetas'
        db.delete_table(u'app_recetas')

        # Removing M2M table for field materia_prima on 'Recetas'
        db.delete_table(db.shorten_name(u'app_recetas_materia_prima'))

        # Deleting model 'Unidades_Presentacion'
        db.delete_table(u'app_unidades_presentacion')

        # Deleting model 'Productos'
        db.delete_table(u'app_productos')

        # Deleting model 'Materia_Prima'
        db.delete_table(u'app_materia_prima')

        # Deleting model 'Clientes'
        db.delete_table(u'app_clientes')

        # Deleting model 'Ventas'
        db.delete_table(u'app_ventas')

        # Deleting model 'Categorias'
        db.delete_table(u'app_categorias')

        # Deleting model 'Proveedores'
        db.delete_table(u'app_proveedores')

        # Removing M2M table for field productos on 'Proveedores'
        db.delete_table(db.shorten_name(u'app_proveedores_productos'))


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
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
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
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Clientes']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.FloatField', [], {}),
            'subtotal': ('django.db.models.fields.FloatField', [], {}),
            'totalcantidad': ('django.db.models.fields.FloatField', [], {})
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