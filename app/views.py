from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def topic_modelform(request):
    TMFO=ModelTopicForm()
    d={'form':TMFO}
    if request.method=='POST':
        FD=ModelTopicForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Topic is inserted by using Model Form ')
    return render(request,'topic_modelform.html',d)

def webpage_modelform(request):
    WMFO=ModelWebpageForm()
    d={'form':WMFO}

    if request.method=='POST':
        FD=ModelWebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Webpage is inserted by using Model Forms')
    return render(request,'webpage_modelform.html',d)

def insert_access(request):
    ao=Model_Access()
    d={'form':ao}
    if request.method=='POST':
        ad=Model_Access(request.POST)
        if ad.is_valid():
            ad.save()
            return HttpResponse('Accessrecord data is inserted')
    return render(request,'insert_access.html',d)