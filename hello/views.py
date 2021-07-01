from django.shortcuts import render
from django.http import HttpResponse

#92ページ
def index(request):
    params = {
        'title':'hello/Index',
        'msg':'お名前は?',
    }
    return render(request, 'hello/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは' + msg + 'さん',
        
    }
    return render(request, 'hello/index.html', params)





'''
def index(request):
    params = {
        'title':'hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
    }
    
    return render(request, 'hello/index.html', params)
    
def next(request):
    params = {
        'title':'hello/Next',
        'msg':'これは、もう一つのページです。',
        'goto':'index',
    }
    
    return render(request, 'hello/index.html', params)
'''