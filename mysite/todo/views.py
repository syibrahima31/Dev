from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.

def index(request): 
    taches = Todo.objects.all().order_by('id')
    return render(request, "todo/index.html", {"taches":taches})



def record(request, pk): 
    return HttpResponse(f"Page {pk}")


