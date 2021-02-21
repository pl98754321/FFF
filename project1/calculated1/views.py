from django.shortcuts import render
from FunctionPL import pluemfunction as pl
# Create your views here.
def cal1(request):
    if request.POST.get('number',2) == '':
        n = range(3)
    else :
        n = range(int(request.POST.get('number',2))+1)
    return render(request,'index.html',{'n':n})

def showtest(request):
    namefriend = request.POST.get('name',0)
    innamefriend = request.POST.get('inname',0)
    return render(request,'test.html',{'namefriend':namefriend,'innamefriend':innamefriend})

#def show(request):
    