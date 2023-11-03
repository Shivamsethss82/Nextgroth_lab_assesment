from django.urls import path
from problem_2 import views

urlpatterns = [
    path('', views.home, name="home"),
]