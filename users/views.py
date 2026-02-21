from django.shortcuts import render,redirect 
from . forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    form=RegisterForm() 
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect ('login_page')
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')

@login_required
def profile(request):
    return render (request,'users/profile.html')

