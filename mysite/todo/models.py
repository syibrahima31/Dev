from django.db import models

# Create your models here.

class Todo(models.Model): 
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    completed = models.BooleanField()
    
    def __str__(self): 
        return f"{self.name}"


