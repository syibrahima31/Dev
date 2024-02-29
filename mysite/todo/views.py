from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Todo
from .forms import UpdateTodoForm, AddTodoForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST": 
        form = UpdateTodoForm(data=request.POST, instance=todo)
        if form.is_valid(): 
            form.save()
            messages.success(request, "Modification  réussie ")
            return redirect('index')
        else: 
            return HttpResponse("error")
        
    else: 
        form = UpdateTodoForm(initial={"name":todo.name})
        return render(request, "todo/update.html", {"form":form, 'id':todo.id})
    


def add(request): 
    if request.method == "POST": 
        form = AddTodoForm(data=request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'todo ajouté !')
            return redirect('index')
        else: 
            messages.error(request, 'erreur ajout')
            return redirect('index')
    else: 
        form = AddTodoForm()
        return render(request, 'todo/add.html', {'form':form})


def login_user(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None: 
                login(request, user)
                messages.success(request, "Connexion reussie")
                return redirect('index')
            else: 
                messages.error(request,"Connexion echoué")
                return redirect('login_user')
        
    else: 
        form = AuthenticationForm()
        return render(request, "todo/login.html", {"form":form})


def logout_user(request): 
    logout(request)
    return redirect(login_user)