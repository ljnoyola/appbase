# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractBaseUser, _user_has_perm, PermissionsMixin, _user_has_module_perms
from managers import UsuarioManager
from django.db.models.signals import *
from django.dispatch import receiver
from django.core.validators import RegexValidator
from datetime import datetime
from choices import *
try:
	from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
	from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import reversion
from django.db.models.signals import pre_delete, post_save
from django.contrib.admin.models import LogEntry, DELETION, ADDITION, CHANGE
from django.utils.encoding import force_text
import inspect
from django.core.handlers.wsgi import WSGIRequest
from reversion.admin import VersionAdmin
from reversion.models import Version, Revision
import json

class Usuario(AbstractBaseUser, PermissionsMixin):
	usuario = models.CharField(max_length=35, unique=True, db_index=True)
	perfil  = models.CharField(max_length=25, choices=Perfiles)
	email = models.EmailField(max_length=50, unique=True)
	activo = models.BooleanField(default=True, help_text='Activa un usuario para poder entrar en el sistema')
	administrador = models.BooleanField(default=False, help_text='Que usuarios se les permite entrar al administrador')
	objects = UsuarioManager()
	USERNAME_FIELD = 'usuario'
	def get_full_name(self):
		return self.usuario + ' ' + self.perfil
	def get_short_name(self):
		return self.usuario
	def __unicode__(self):
		return self.usuario
	def has_perm(self, perm, obj=None):
		if self.is_superuser:
			return True
		return _user_has_perm(self, perm, obj=obj)
	def has_module_perms(self, app_label):
		return True
	@property
	def is_staff(self):
		return self.administrador
	@property
	def is_active(self):
		return self.activo
	def __unicode__(self) :
	    return '%s' % (self.usuario)
class Categorias(models.Model):
	nombre = models.CharField(max_length=50)    
	def __unicode__(self):
		return self.nombre
	def productos(self):
		return Productos.objects.filter(categoria=self)

class Productos(models.Model):
	nombre = models.CharField('Nombre', max_length=50)
	descripcion = models.TextField('Descripción',null=True, blank=True )
	precio = models.FloatField(help_text="No escribir signo de $")
	categoria = models.ForeignKey('Categorias')
	cantidad = models.IntegerField(default=0)
	def __unicode__(self):
		return self.nombre + "    $" +str(self.precio)

class Proveedores(models.Model):
	nombre = models.CharField(max_length=50)
	rfc = models.CharField('RFC', max_length=50, null=True, blank=True )
	direccion = models.TextField('Dirección')
	telefono = models.CharField('Teléfono', max_length=50, default='55-')
	contacto = models.CharField(max_length=50)
	email = models.CharField(max_length=50, default='ejemplo@mail.com')
	productos = models.ManyToManyField("Productos")
	def __unicode__(self):
		return self.nombre	+ self.telefono

class Unidades_Presentacion(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.FloatField()
    def __unicode__(self):
		return self.nombre

class Materia_Prima(models.Model):
	nombre = models.CharField(max_length=50)
	costo = models.FloatField()
	proveedor = models.ForeignKey('Proveedores')
	unidad_presentacion = models.ForeignKey('Unidades_Presentacion')
	def __unicode__(self):
		return self.nombre

class Clientes(models.Model):
	nombre = models.CharField(max_length=50)
	a_paterno = models.CharField('Apellido Paterno', max_length=50)
	a_materno = models.CharField('Apellido Materno', max_length=50)
	rfc = models.CharField('RFC', max_length=50, null=True, blank=True)
	telefono = models.CharField('Teléfono', max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	def __unicode__(self):
		return self.nombre + self.a_paterno + self.a_materno + self.rfc + self.telefono + self.email


class Ventas(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	ventasproducto = models.ManyToManyField('VentasProducto')
	cliente = models.ForeignKey('Clientes')
	subtotal = models.FloatField(help_text="No escribir signo de $")
	iva = models.FloatField(help_text="No escribir signo de $")
	totalcantidad = models.FloatField('Total', help_text="No escribir signo de $")
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.fecha) + self.cliente.nombre + str(self.totalcantidad)

class VentasProducto(models.Model):
	claveproducto= models.ForeignKey("Productos")
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.id) + ' ' + self.claveproducto.nombre + " " + str(self.cantidad)
		
class Recetas(models.Model):
	producto = models.ForeignKey('Productos')
	materia_prima = models.ManyToManyField("Materia_Prima")
	unidad_de_medida = models.CharField(max_length=50,  choices = unidadespresentacion)
	cantidad = models.FloatField()
	def __unicode__(self):
		return self.producto.nombre + self.materia_prima.all()[0].nombre

class Contacto(models.Model):
	nombre = models.CharField('Nombre', max_length=50)
	email = models.EmailField(max_length=50)
	comentario = models.TextField('Comentario', max_length=50)
	def __unicode__(self):
		return self.nombre	+ self.email + self.comentario


