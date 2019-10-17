from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def createaccount(request):
    return HttpResponse('<h1>Create Account</h1>')