from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property
# Create your views here.
class Propertylist(ListView):
    model = Property
    

class Propertydetails(DetailView):
    model = Property
   
        