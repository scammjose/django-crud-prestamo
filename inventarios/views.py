from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def inventarios(request):
    return render(request,'inventarios/inventarios.html')