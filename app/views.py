from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def crazy(request):
    return HttpResponse('<h1 style="background-color:blue;"><marquee>Iam very crazy....</h1></marquee>')
