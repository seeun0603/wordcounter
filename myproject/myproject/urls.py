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
import myapp.views
import helloworld.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home, name='home'),
    #라우트, 라우트 조건일때 myapp안에 있는 views라는 파일안에 home라는 것을 실행시켜라, 이 경로 자체를 home라고 부르겠다.
    #url의 이름은 함수의 이름과 동일하게 만든다.
    #/뒤에 이름을 쓰면 그 뒤에 나오기를 바라는 페이즈를 보여준다
    # ex) 127.0.0.1/admin/라면 admin을 입력했을 때 그 페이지를 보여주기를 원한다. 
    path('hello/',helloworld.views.hello, name='intro'),
    path('example/',include('secondapp.urls'), name='second'),
    #url과 url끼리 연결해준거 
]