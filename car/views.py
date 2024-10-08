from django.shortcuts import render
from . import forms
# Create your views here.
def add_car(request):
    car_form=forms.CarForm()
    return render(request,'add_car.html',{'form':car_form})


