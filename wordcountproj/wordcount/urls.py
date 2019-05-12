from django.contrib import admin
from django.urls import path
import wordcountex.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcountex.views.home, name ='home'),
    path('about/', wordcountex.views.about, name='about'),
    path('wordcount/', wordcountex.views.wordcount, name='wordcount'),
    path('result/', wordcountex.views.result, name='result'),
]
