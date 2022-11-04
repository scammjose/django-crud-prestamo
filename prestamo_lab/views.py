from django.shortcuts import redirect, render
from django.db import connection
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from laboratorio.models import Laboratorios

# Create your views here.
@login_required(login_url='login')
def prestamo_lab(request):
    cursor=connection.cursor()
    cursor.execute("call buscar_prestamo_lab()")
    results=cursor.fetchall()
    return render(request,'prestamo/prestamo_lab.html',{'data':results})

@login_required(login_url='login')
def prestar_lab(request):
    data=Laboratorios.objects.filter(status=0)
    if request.method=="POST":
        if request.POST.get('matricula') and request.POST.get('codigo'):
            matricula=request.POST.get('matricula')
            codigo=request.POST.get('codigo')
            # prueba de codigo de validacion de matricula
            total=connection.cursor()
            total.execute("call buscar_matricula("+matricula+")")
            result=total.fetchall()
            for r in result:
                if r[0]==1:
                    cursor=connection.cursor()
                    cursor.execute("call insertar_prestamo_lab('"+matricula+"','"+str(codigo)+"')")
                    messages.success(request,'Prestamo exitoso')
                    return redirect('prestamo_lab')
                messages.error(request,'Docente no encontrado')
    return render(request,'prestamo/prestar_lab.html',{'data':data})

@login_required(login_url='login')
def quitar_lab(request,id):
    cursor=connection.cursor()
    cursor.execute("call quitar_prestamo_lab("+str(id)+")")
    messages.success(request,'Devolución exitosa')
    return redirect('prestamo_lab')

