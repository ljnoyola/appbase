from django.contrib import admin
from models import *

class ProveedoresAdmin(admin.ModelAdmin):
	filter_horizontal	 = ['productos']


class ProductosAdmin(admin.ModelAdmin):
   fieldsets = (
			        ('Nombre del Producto', {
			            		'fields': ('nombre',)
			        		}),
			        ('Descipciones', {
            					'classes': ('wide', 'extrapretty'),
            					'description': ('CApturar los datos del producto'),
			            		'fields': ('descripcion', 'precio', 'categoria', 'cantidad')
			        }),
			    )

   list_display = ('nombre', 'id', 'precio')

   list_editable = ('precio',)

   search_fields = ('nombre',)

   list_filter = ('categoria','nombre')

class Materias_primasAdmin(admin.ModelAdmin):
	fieldsets = (
			        ('Nombre del Producto', {
			            		'fields': ('nombre',)
			        		}),
			        ('Proveedor', {
            					'classes': ('collapse',),
            					'description': ('Capturar los datos de la Materia Prima'),
			            		'fields': ('costo', 'proveedor', 'unidad_presentacion')
			        }),
			    )

class RecetasAdmin(admin.ModelAdmin):
	filter_horizontal	 = ['materia_prima']


admin.site.register(Categorias)
admin.site.register(Productos,  ProductosAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Unidades_Presentacion)
admin.site.register(Materia_Prima, Materias_primasAdmin)
admin.site.register(Clientes)
admin.site.register(Ventas)
admin.site.register(Recetas, RecetasAdmin)

# Register your models here.
