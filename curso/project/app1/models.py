# -*- encoding: utf-8 -*-
from django.db import models
from datetime import date
from opciones import *

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)    
    def __unicode__(self):
		return self.nombre

class Productos(models.Model):
	nombre = models.CharField('Nombre', max_length=50)
	descripcion = models.TextField('Descripción',null=True, blank=True )
	precio = models.FloatField(help_text="No escribir signo de $")
	categoria = models.ForeignKey('Categorias')
	cantidad = models.IntegerField()
	def __unicode__(self):
		return self.nombre + str(self.precio)

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
	cliente = models.ForeignKey('Clientes')
	subtotal = models.FloatField(help_text="No escribir signo de $")
	iva = models.FloatField(help_text="No escribir signo de $")
	totalcantidad = models.FloatField('Total', help_text="No escribir signo de $")
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.fecha) + self.cliente.nombre + str(self.totalcantidad)
		
class Recetas(models.Model):
	producto = models.ForeignKey('Productos')
	materia_prima = models.ManyToManyField("Materia_Prima")
	unidad_de_medida = models.CharField(max_length=50,  choices = unidadespresentacion)
	cantidad = models.FloatField()
	def __unicode__(self):
		return self.producto.nombre + self.materia_prima.all()[0].nombre



