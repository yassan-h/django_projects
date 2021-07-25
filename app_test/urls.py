from django.urls import path
from app_test import views

app_name = 'app_test'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('add/', views.add, name='add')
]
