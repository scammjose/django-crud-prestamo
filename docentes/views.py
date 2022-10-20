from contextvars import Context
from datetime import datetime
from django.shortcuts import redirect, render

from docentes.models import Docentes
from .forms import DocentesForm

# Create your views here.
def docentes(request):
    docentes=Docentes.objects.all()
    return render(request,'docentes/docentes.html',{'docentes':docentes})

def inicio(request):
    fecha=datetime.now()
    return render(request,'docentes/inicio.html',{'fecha':fecha})

def crear(request):
    formulario=DocentesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('docentes')
    return render(request,'docentes/crear.html',{'formulario':formulario})

def editar(request,id):
    docente=Docentes.objects.get(id=id)
    formulario=DocentesForm(request.POST or None, request.FILES or None, instance=docente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('docentes')
    return render(request,'docentes/editar.html',{'formulario':formulario})

def borrar(request,id):
    docente=Docentes.objects.get(id=id)
    docente.delete()
    return redirect('docentes')

def redireccion(request):
    return redirect('inicio')