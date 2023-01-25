from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    return render(request,'display_topic.html')

def display_webpage(request):
    qsw=Webpage.objects.all()
    d={'webpage':qsw}
    return render(request,'display_webpage.html',d)

def display_acces(request):
    qsa=AcessRecord.objects.all()
    d={'access':qsa}
    return render(request,'display_acces.html',d)