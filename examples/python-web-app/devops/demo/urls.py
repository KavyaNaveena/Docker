from django.urls import path

from . import views

urlpatterns = [
    path('http://54.227.225.32/', views.index, name='index'),
]
