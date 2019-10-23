from django.urls import path
from . import views

urlpatterns = [
    path('', views.createaccount, name='katz-createaccount'),
]