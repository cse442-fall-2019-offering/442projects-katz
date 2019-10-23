from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
    else:
        form = UserCreationForm()
    return render(request, 'users/createAccount.html', {'form': form})
