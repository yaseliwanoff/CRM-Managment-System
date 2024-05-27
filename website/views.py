from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    # Проверка входа в систему
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Аутенификация
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in website!")
            return redirect('home')
        else:
            messages.success(request, 'There was an error loggin, please try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Аутентификация и вход в систему
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have siccessfully registered in website')
            return redirect('home')
    else:
        form = SignUpForm()  # запрос не идет в случае не заполненной формы
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})
