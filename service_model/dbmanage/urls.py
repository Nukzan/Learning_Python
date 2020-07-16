from dbmanage import views
from django.urls import path
urlpatterns = [
        path("", views.home, name = "hello-home"),
        path("list/", views.list, name = "list"),
        ]
