from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic data inserted successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        w=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        w.save()
        return HttpResponse('webpage data is inserted successfully')

    return render(request,'insert_webpage.html',d)

def insert_access_records(request):
    topic=Topic.objects.all()
    d={'topic':topic}
    Webpage=webpage.objects.all()
    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        dt=request.POST['dt']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        w=webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        w.save()
        A=access_records.objects.get_or_create(name=w,date=dt)[0]
        A.save()
        return HttpResponse('accessrecords data is successfully inserted')
    return render(request,'insert_access_records.html',d)

def select_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}

    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=webpage.objects.none()
        for i in tn:
            webpages=webpages|webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,'display_webpage.html',data)
    return render(request,'select_topic.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    
    return render(request,'checkbox.html',d)
