from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',patient_list,name='list'),
    path('detail/<str:pk>/',patient_detail,name='detail'),
    path('update/<str:pk>/',patient_update,name='update'),
    path('delete/<str:pk>/',patient_delete,name='delete'),
    path('create',patient_create,name='create'),
    path('detail/<str:pk>/medicine/',medicine_list,name='medlist'),
    path('detail/<str:pk>/medicine/create',medicine_create,name='medcreate'),
]
