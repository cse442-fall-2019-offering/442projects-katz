from django.shortcuts import render

info = [
    {}
]

# Create your views here.
def mainpage(request):
    context = {
        'information': info
    }
    return render(request, 'templates/mainpge.html', context)

def profile(request):
    context = {
        'information': info
    }
    return render(request, 'templates/profile.html', context)

def createAccount(request):
    context = {
        'information': info
    }
    return render(request, 'templates/createAccount.html', context)

def login(request):
    context = {
        'information': info
    }
    return render(request, 'templates/Login.html', context)

def classStudy(request):
    context = {
        'information': info
    }
    return render(request, 'templates/Class.html', context)

def team(request):
    context = {
        'information': info
    }
    return render(request, 'templates/Team.html', context)