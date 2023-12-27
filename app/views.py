from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def htmlforms(request):
    if request.method=="POST":
        username=request.POST['un']
        password=request.POST.get('pw')
        return HttpResponse('Data is inserted')
    return render(request,'htmlforms.html')


def create_school(request):
    if request.method=="POST":
        sn=request.POST['sn']
        sl=request.POST['sl']
        sp=request.POST.get('sp')

        SO=School.objects.get_or_create(sname=sn,sloc=sl,sprincipal=sp)[0]
        SO.save()

        return HttpResponse('School data is inserted')
    return render(request,'create_school.html')
