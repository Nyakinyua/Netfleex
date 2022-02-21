from django import views
from django.urls import path
from . import views

app_name='netfleex'

urlpatterns = [
    path('',views.home,name='home')

]

