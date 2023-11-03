from django.urls import path
from problem_1 import views

urlpatterns = [
    path('', views.extract_numbers, name="extract_numbers"),
]