from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Salon,Booking
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    salons=Salon.objects.all()   
    return render(request,"booking/index.html",{"salons":salons})


def detail(request,id):
    salon=Salon.objects.get(id=id)
    return render(request,'booking/detail.html',{"salon":salon})

@login_required
def booking_form(request):
    if request.method=="POST":
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        date=request.POST.get('date',"")
        booking=Booking(name=name,email=email,date=date)
        messages.success(request,f"Booked at {date}")
        booking.save()
        return redirect('booking:index')


    return render(request,'booking/booking_form.html')



