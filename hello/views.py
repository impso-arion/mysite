from django.shortcuts import render
from django.http import HttpResponse

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