from hello import views
from django.urls import path
urlpatterns = [
        path("", views.home, name = "hello-home"),
        path("form/", views.form, name = "form"),
        path("result/", views.result, name = "result"),
        # path("template/", views.template, name = "template"),
        # path("templatefromsite/", views.templatefromsite),
        # path("bootstrapTemp/", views.bootstrapTemp),
        ]
