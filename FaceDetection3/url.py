from urllib import request
from django.contrib import admin
from django.urls import path
from FaceDetection3 import views  

urlpatterns = [
    path('', views.index,name='FaceDetection3'),
    path('output', views.output,name='output'),  
]