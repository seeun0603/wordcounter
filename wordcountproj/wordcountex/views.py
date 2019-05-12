from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wordcount(request):
    return render(request, 'wordcount.html')

def result(request):
    text = request.GET['fulltext'] 
    #글 전체를 의미함
    words = text.split() 
    word_dic ={}
   
    for i in words:
        if i in word_dic:
            word_dic[i] +=1
        else:
            word_dic[i] = 1 

    return render(request, 'result.html',{'full':text, 'total':len(words), 'dic': word_dic.items()}) 
    #세번째 인자는 사전형 객체로 딕션너리
    #.items() 안의 변수를 한번에 넘길때