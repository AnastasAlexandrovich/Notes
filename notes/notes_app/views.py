import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm


def index(request):
    return render(request, 'notes_app/index.html')


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('notes_app/index')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
            else:
                #если не зареган
                return redirect('/notes_app')
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def add_note(request):
        return render(request, 'notes_app/add-note.html')


def save_note(request):
    # текст заметки
    text = request.POST['note-text']
    print('miu: ' + text)

    #поменять то что нужно вернуть
    return HttpResponse(status=200)