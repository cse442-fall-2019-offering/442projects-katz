from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='katz-login'),
]