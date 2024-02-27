from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.

def index(request): 
    taches = Todo.objects.all().order_by('id')
    return render(request, "todo/index.html", {"taches":taches})



def record(request, pk): 
    todo = Todo.objects.get(id=pk)
    return render(request, "todo/todo.html", {"tache":todo})


def delete(request, pk): 
    tache = Todo.objects.get(id=pk)
    tache.delete()
    return redirect('index')