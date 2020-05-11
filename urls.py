from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("list/",views.listofmovies,name="listofmovies"),
    path("player/<name>",views.player,name="player")
]