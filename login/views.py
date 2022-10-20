from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistroForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def registro(request):
    if request.method=='POST':
        form=UserRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,'Usuario '+username+' creado')
            return redirect('inicio')
    else:
        form=UserRegistroForm()
    context={'form':form}
    return render(request,'registro/registro.html',context)