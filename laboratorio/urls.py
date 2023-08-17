from django.contrib import admin
from django.urls import path, include
from . import views
from .views import InicioPageView

urlpatterns = [
    path('', views.insertar_lab, name='insertar-lab'),
    path('mostrar/', views.mostrar_lab, name='mostrar-lab'),
    path('editar/<int:pk>', views.editar_lab, name='editar-lab'),
    path('editar/actualizarlaboratorio/<int:id>', views.actualizarlaboratorio, name ='actualizarlaboratorio'),
    path('eliminar/<int:pk>', views.eliminar_lab, name='eliminar-lab'),
   
    #path("detalle/<int:pk>", views.laboratorio_detalle, name="laboratorio-detalle"),
    path("inicio/", InicioPageView.as_view(), name="inicio"),
    #path("acerca-de/", AcercaPageView.as_view(), name="acerca-de"),
]