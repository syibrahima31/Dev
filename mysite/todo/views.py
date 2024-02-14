from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request): 
    data = [
        {"nom":"Abdou", "age":20, "sexe":"M"},
        {"nom":"Felix", "age":22, "sexe":"M"},
        {"nom":"Nabou", "age":19, "sexe":"F"},
        {"nom":"Eric", "age":28, "sexe":"M"},
        {"nom":"Jessica", "age":30, "sexe":"F"}
        ]
    return render(request, "todo/index.html", {"donnee":data})
