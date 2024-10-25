from django.contrib import admin 
from .models import Laboratorio, DirectorGeneral, Producto
admin.site.site_header = 'Django administration' 
admin.site.index_title = 'Panel de control Proyecto Django' 
admin.site.site_title = 'Administrador Django' 


class AdminLaboratorio(admin.ModelAdmin): 
    model = Laboratorio
    list_display = ('lab_id','lab_nombre','lab_ciudad','lab_pais')

class AdminDirectorGeneral(admin.ModelAdmin): 
    model = DirectorGeneral
    list_display = ('id','nombre','laboratorio','especialidad')
    
class AdminProducto(admin.ModelAdmin): 
    model = Producto
    list_display = ('id','nombre', 'laboratorio','f_fabricacion','p_costo','p_venta')




admin.site.register(Laboratorio, AdminLaboratorio) 
admin.site.register(DirectorGeneral, AdminDirectorGeneral) 
admin.site.register(Producto, AdminProducto) 
