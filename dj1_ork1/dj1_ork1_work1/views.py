from os import name
from django.contrib.admin import autodiscover
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'index.html')

def nameAticle(request):
    #data from aticlename
    name = request.POST["Aticle"]
    inside = request.POST["insideAticle"]
    return render(request,'nameAticle.html',{"nameindex2":name,"insideindex":inside})