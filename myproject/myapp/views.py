from django.shortcuts import render

# Create your views here.

# reqeust가 들어왔을때 home.html을 가져다줘라는 함수
def home(request):
    return render(request,'home.html')