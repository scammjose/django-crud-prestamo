from datetime import datetime
from django.shortcuts import redirect, render
from docentes.models import Docentes
from .forms import DocentesForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def docentes(request):
    docentes=Docentes.objects.all()
    return render(request,'docentes/docentes.html',{'docentes':docentes})

@login_required(login_url='login')
def inicio(request):
    fecha=datetime.now()
    return render(request,'docentes/inicio.html',{'fecha':fecha})

@login_required(login_url='login')
def crear(request):
    formulario=DocentesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'El docente ha sido creado correctamente')
        return redirect('docentes')
    return render(request,'docentes/crear.html',{'formulario':formulario})

@login_required(login_url='login')
def editar(request,id):
    docente=Docentes.objects.get(id=id)
    formulario=DocentesForm(request.POST or None, request.FILES or None, instance=docente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request,'El docente ha sido actualizado correctamente')
        return redirect('docentes')
    return render(request,'docentes/editar.html',{'formulario':formulario})

@login_required(login_url='login')
def borrar(request,id):
    docente=Docentes.objects.get(id=id)
    docente.delete()
    messages.success(request,'El docente ha sido eliminado correctamente')
    return redirect('docentes')

@login_required(login_url='login')
def redireccion(request):
    return redirect('inicio')