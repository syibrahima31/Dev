from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('record/<int:pk>/', views.record, name="record"), 
    path('delete/<int:pk>/', views.delete, name="delete" )

]
