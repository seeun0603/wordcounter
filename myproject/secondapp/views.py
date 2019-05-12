from django.shortcuts import render

# Create your views here.
def main(request):
    text = '저는 멋사 7기 심세은입니다.'
    name = '안녕하세요!'
    context ={'name': name ,'text': text}
    fruit =['apple','pear','oranage','banana']
    return render(request,'secondapp/result.html',{'fruit':fruit})

def result(request):
    text = request.GET.get('text')
    words = text.split(' ')
    wordcnt = {}
    for i in words:
        if i in wordcnt:
            wordcnt[i] += 1
        else:
            wordcnt[i] = 1

    context ={'text': text,'words':words, 'wordcnt': wordcnt, 'wordcnt_item':wordcnt.items()}
    return render(request,'secondapp/result.html',context)

def menu(request):
    text ="menu입니다"
    context ={'text':text}
    return render(request, "secondapp/menu.html",context)