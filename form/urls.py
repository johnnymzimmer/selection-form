from django.urls import path
from . import views

urlpatterns = [
    path('', views.selection_form, name='selection_form'),
]
