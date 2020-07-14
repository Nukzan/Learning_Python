

from organization import views
from django.urls import path
from django.urls import include

urlpatterns = [
        path("", views.home, name = "organization-home"),
]
