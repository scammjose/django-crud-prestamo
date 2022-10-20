from django.db import connection
from django.shortcuts import redirect, render
from equipos.models import Equipos
from prestamo.models import Prestamo


# Create your views here.
def prestamo(request):
    # prestamo=Prestamo.objects.all()

    # Inner Join con Stored Procedure
    cursor=connection.cursor()
    cursor.execute("call buscar_prestamo()")
    results=cursor.fetchall()
    return render(request,'prestamo/prestamo.html',{'data':results})


def prestar(request):
    data=Equipos.objects.all()
    if request.method=="POST":
        if request.POST.get('matricula') and request.POST.getlist('codigo[]'):
            matricula=request.POST.get('matricula')
            codigo=request.POST.getlist('codigo[]')
            mapear=map(int,codigo)
            items=list(mapear)
            for item in items:
                cursor=connection.cursor()
                cursor.execute("call insertar_prestamo('"+matricula+"','"+str(item)+"')")
            return redirect('prestamo')
    return render(request,'prestamo/prestar.html',{'data':data})

def quitar(request,id):
    cursor=connection.cursor()
    cursor.execute("call quitar_prestamo("+str(id)+")")
    return redirect('prestamo')