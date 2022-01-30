from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('sign_up/', views.Sign_up, name='Sign_up'),
    path('sign_in/', views.Sign_in, name='Sign_in'),
    path('app_in/', views.appin, name='App_in'),
    path('add_friend/', views.add_friend, name='Addfriend'),
    path('add/<int:Id>', views.Add, name='Add'),
]