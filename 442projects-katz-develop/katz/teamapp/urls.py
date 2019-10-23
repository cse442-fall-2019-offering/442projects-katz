from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='teamapp-login'),
    path('createaccount/', views.createaccount, name='teamapp-createaccount'),
]
