from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def htmlforms(request):
    if request.method=="POST":
        username=request.POST['un']
        password=request.POST.get('pw')
        return HttpResponse('Data is inserted')
    return render(request,'htmlforms.html')