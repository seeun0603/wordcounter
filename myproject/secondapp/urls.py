"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="result"),
    path('result/', views.result, name ="result"),
    path('meun/', views.menu, name='meun'),
    #이미 처음 url에 의해 example/를 걸러졌기 때문에 비워서 사용
]