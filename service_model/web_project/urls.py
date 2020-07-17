"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('myhello/', include('myhello.urls')),
    path('organization/', include('organization.urls')),
    path('dbmanage/', include('dbmanage.urls')),
    ]

from crawling.crawling_tasks import task_hello  # 호출하는 부분
task_hello()
from crawling.crawling_tasks import task_crawling_daum  # 호출하는 부분
task_crawling_daum()
