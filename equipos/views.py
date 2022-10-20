from django.shortcuts import redirect, render
from equipos.models import Equipos
from .forms import EquiposForm

# Create your views here.
def equipos(request):
    equipos=Equipos.objects.all()
    # equipos=Equipos.objects.filter(status=0)
    return render(request,'equipos/equipos.html',{'equipos':equipos})

def crear(request):
    formulario=EquiposForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('equipos')
    return render(request,'equipos/crear.html',{'formulario':formulario})

def editar(request,id):
    equipo=Equipos.objects.get(id=id)
    formulario=EquiposForm(request.POST or None, request.FILES or None, instance=equipo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('equipos')
    return render(request,'equipos/editar.html',{'formulario':formulario})

def borrar(request,id):
    equipo=Equipos.objects.get(id=id)
    equipo.delete()
    return redirect('equipos')