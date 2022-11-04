from django.contrib import messages
from django.shortcuts import redirect, render

from docentes.models import Docentes
from .forms import UserRegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='login')
def registro(request):
    if request.method=='POST':
        form=UserRegistroForm(request.POST or None)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,'Usuario '+username+' creado correctamente')
            return redirect('inicio')
    else:
        form=UserRegistroForm()
    context={'form':form}
    return render(request,'registro/registro.html',context)

@login_required(login_url='login')
def usuario(request,username):
    usuario=User.objects.get(username=username)
    return render(request,'usuario/usuario.html',{'usuario':usuario})