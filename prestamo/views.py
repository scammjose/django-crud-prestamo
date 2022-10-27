from django.db import connection
from django.shortcuts import redirect, render
from django.template import RequestContext
from equipos.models import Equipos
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def prestamo(request):
    # prestamo=Prestamo.objects.all()

    # Inner Join con Stored Procedure
    cursor=connection.cursor()
    cursor.execute("call buscar_prestamo()")
    results=cursor.fetchall()
    return render(request,'prestamo/prestamo.html',{'data':results})

@login_required(login_url='login')
def prestar(request):
    data=Equipos.objects.all()
    if request.method=="POST":
        if request.POST.get('matricula') and request.POST.getlist('codigo[]'):
            matricula=request.POST.get('matricula')
            codigo=request.POST.getlist('codigo[]')
            # prueba de codigo de validacion de matricula
            total=connection.cursor()
            total.execute("call buscar_matricula("+matricula+")")
            result=total.fetchall()
            for r in result:
                if r[0]==1:
                    mapear=map(int,codigo)
                    items=list(mapear)
                    for item in items:
                        cursor=connection.cursor()
                        cursor.execute("call insertar_prestamo('"+matricula+"','"+str(item)+"')")
                    messages.success(request,'Prestamo exitoso')
                    return redirect('prestamo')
                messages.error(request,'Docente no encontrado')
    return render(request,'prestamo/prestar.html',{'data':data})

@login_required(login_url='login')
def quitar(request,id):
    cursor=connection.cursor()
    tiempo=connection.cursor()
    tiempo.execute("call tiempo("+str(id)+")")
    result=tiempo.fetchall()
    for r in result:
        # print(r[0])
        if r[0]==1:
            cursor.execute("call quitar_prestamo("+str(id)+")")
            messages.success(request,'Devolución exitosa')
            return redirect('prestamo')
        else:
            cursor.execute("call sancion("+str(id)+")")
            cursor.execute("call sancion_quitar_prestamo("+str(id)+")")
            messages.error(request,'Entrega tardía, usuario bloqueado')
            return redirect('prestamo')