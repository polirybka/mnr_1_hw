from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("task/", views.task, name="task"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("list/", views.list, name="list"),
    path("kvest/kvest1/", views.kvest1, name="kvest1"),
    path("kvest/kvest2/", views.kvest2, name="kvest2"),
]



