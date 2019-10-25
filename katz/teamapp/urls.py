from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<int:idOfClass>/', views.classpage, name='classpage'),
]