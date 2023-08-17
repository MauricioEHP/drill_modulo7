from django.shortcuts import render,redirect
from .models import *
from django.views.generic import TemplateView

# Create your views here.

def insertar_lab(request):
    if request.method == "POST":
         lab_nombre = request.POST['lab_nombre']
         lab_ciudad = request.POST['lab_ciudad']
         lab_pais = request.POST['lab_pais']
         laboratorio = Laboratorio(lab_nombre=lab_nombre, lab_ciudad=lab_ciudad, lab_pais=lab_pais)
         laboratorio.save()
         return redirect('mostrar/')
    else:
        return render(request, 'insertar.html')
        

        

def mostrar_lab(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'mostrar.html',{'laboratorio':laboratorios})

def editar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)

    context = {
        'laboratorio': laboratorio,
    }
    return render (request=request, template_name='editar.html', context=context)

def actualizarlaboratorio(request, id):
    id= request.POST['id']
    lab_nombre=request.POST['lab_nombre']
    lab_ciudad=request.POST['lab_ciudad']
    lab_pais=request.POST['lab_pais']
    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.id = id
    laboratorio.lab_nombre = lab_nombre
    laboratorio.lab_ciudad = lab_ciudad
    laboratorio.lab_pais = lab_pais
    laboratorio.save()
    return redirect('/mostrar')

def eliminar_lab(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar-lab')
    context = {
        'laboratorio': laboratorio
    }
    return render(request, 'eliminar.html', context)

class InicioPageView(TemplateView):
    template_name= "inicio.html"

