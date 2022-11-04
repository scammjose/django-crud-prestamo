from django.shortcuts import redirect, render
from equipos.models import Equipos
from .forms import EquiposForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def equipos(request):
    equipos=Equipos.objects.all()
    # equipos=Equipos.objects.filter(status=0)
    return render(request,'equipos/equipos.html',{'equipos':equipos})

@login_required(login_url='login')
def crear(request):
    formulario=EquiposForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Nuevo equipo añadido correctamente')
        return redirect('equipos')
    return render(request,'equipos/crear.html',{'formulario':formulario})

@login_required(login_url='login')
def editar(request,id):
    equipo=Equipos.objects.get(id=id)
    formulario=EquiposForm(request.POST or None, request.FILES or None, instance=equipo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request,'El equipo ha sido actualizado correctamente')
        return redirect('equipos')
    return render(request,'equipos/editar.html',{'formulario':formulario})

@login_required(login_url='login')
def borrar(request,id):
    equipo=Equipos.objects.get(id=id)
    equipo.delete()
    messages.success(request,'Equipo eliminado correctamente')
    return redirect('equipos')