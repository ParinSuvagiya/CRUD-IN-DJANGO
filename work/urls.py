#work
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.reg,name='reg'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('<int:id>',views.update,name='update')
]
