from django.contrib import admin
from .models import *
from django.contrib import messages
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

class BoardsAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'lab_nombre')
    list_display = ('id', 'lab_nombre')
    search_fields = ('id', 'lab_nombre')
    ordering = ('id',)

class BoardAdmin(admin.ModelAdmin):
    readonly_fields = ('id_dir', 'dir_nombre', 'laboratorio' )
    list_display = ('id_dir', 'dir_nombre', 'laboratorio')
    search_fields = ('id_dir', 'dir_nombre', 'laboratorio')
    ordering = ('id_dir',)

class BoardcAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'pro_nombre', 'pro_laboratorio','f_fabricacion','p_costo','p_venta' )
    list_display = ('id', 'pro_nombre', 'pro_laboratorio','f_fabricacion','p_costo','p_venta')
    search_fields = ('id', 'pro_nombre', 'pro_laboratorio','f_fabricacion','p_costo','p_venta')
    ordering = ('id',)

admin.site.register(Laboratorio, BoardsAdmin)
admin.site.register(DirectorGeneral, BoardAdmin )
admin.site.register(Producto, BoardcAdmin)


