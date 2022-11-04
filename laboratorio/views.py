from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from laboratorio.forms import LaboratoriosForm
from laboratorio.models import Laboratorios
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def laboratorios(request):
    laboratorio=Laboratorios.objects.all()
    return render(request,'laboratorios/laboratorios.html',{'laboratorio':laboratorio})

@login_required(login_url='login')
def crear(request):
    formulario=LaboratoriosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'El laboratorio ha sido añadido correctamente')
        return redirect('laboratorios')
    return render(request,'laboratorios/crear_lab.html',{'formulario':formulario})

@login_required(login_url='login')
def editar(request,id):
    laboratorio=Laboratorios.objects.get(id=id)
    formulario=LaboratoriosForm(request.POST or None, request.FILES or None, instance=laboratorio)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request,'El laboratorio ha sido actualizado correctamente')
        return redirect('laboratorios')
    return render(request,'laboratorios/editar_lab.html',{'formulario':formulario})

@login_required(login_url='login')
def borrar(request,id):
    laboratorio=Laboratorios.objects.get(id=id)
    laboratorio.delete()
    messages.success(request,'Laboratorio eliminado correctamente')
    return redirect('laboratorios')