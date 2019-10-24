from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.utils.forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request, f'Account created for {username}!')
            return redirect('http://127.0.0.1:8000')
    else:
        form = SignUpForm()
    return render(request, 'users/createAccount.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')
