from django.urls import path

from thing import views

urlpatterns = [
    path('', views.index, name='index'),
]