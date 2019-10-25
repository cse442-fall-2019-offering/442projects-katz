from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('class/<int:idOfClass>/', views.classpage, name='classpage'),
    path('team/<int:idOfTeam>/', views.teampage, name='teampage'),
    path('user/<str:usrname>/', views.profilepage, name='profilepage'),
    path('team/<int:idOfTeam>/join/', views.jointeam, name='jointeam'),
    path('team/<int:idOfTeam>/leave/', views.leaveteam, name='leaveteam'),
    path('user/myprofilepage', views.myprofilepage, name='myprofilepage'),
]