from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name="login"), 
    path('index/', views.index, name='index'), 
    path('record/<int:pk>/', views.record, name="record"), 
    path('delete/<int:pk>/', views.delete, name="delete" ),
    path('update/<int:pk>/', views.update, name="update" ),
    path('add/', views.add, name="add" ), 
    path('logout/', views.logout_user, name='logout')


]
