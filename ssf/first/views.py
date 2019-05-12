from django.shortcuts import render

# Create your views here.
def main(request):
    text ='come back home'
    fruits = ['apple','orange','banana','pear']
    context = {'text': text,'fruits':fruits}
    return render(request, 'first/index.html',context)

def wordcount(request):
    text = request.GET.get('text') #input의 내이름이 text
    context ={'text':text}
    return render(request, 'first/wordcount.html', context )