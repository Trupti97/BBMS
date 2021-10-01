from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.events, name='events'),
    path('bank', views.bank, name='bank'),
    path('contact', views.contact, name='contact'),
   
]