from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read) # id 값을 인자로 받을수 있음
]
