from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def createaccount(request):
    return render(request, 'katz/createAccount.html')
