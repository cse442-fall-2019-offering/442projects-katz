from django.urls import path
from . import views

#Url paths for every page in teamapp
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('class/<int:idOfClass>/', views.classpage, name='classpage'),
    path('team/<int:idOfTeam>/', views.teampage, name='teampage'),
    path('user/<str:usrname>/', views.profilepage, name='profilepage'),
    path('team/<int:idOfTeam>/join/', views.jointeam, name='jointeam'),
    path('team/<int:idOfTeam>/leave/', views.leaveteam, name='leaveteam'),
    path('user/myprofilepage', views.myprofilepage, name='myprofilepage'),
    path('createaccount/', views.createAccount, name='createaccount'),
    path('team/<int:idOfTeam>/kick/<str:usr>/', views.kickMember, name='kickmember'),
    path('team/<int:idOfTeam>/edit', views.teampageEdit, name='teampageEdit'),
]
