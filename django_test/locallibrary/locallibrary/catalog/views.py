from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    print("请耐心等待")
    return render(request,'index.html')
    # return HttpResponse("Hello World")