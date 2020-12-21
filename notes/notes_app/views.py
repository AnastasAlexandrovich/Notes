import json
from django.utils import timezone

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import User, Note


def index(request):
    if request.user.is_authenticated:
        count = Note.objects.filter(user_email=request.user.email).count()
        print(str(request.user.email))
        print(str(request.user.email))
        return render(request, 'notes_app/index.html', {'count': count})
    else:
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
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def add_note(request):
    return render(request, 'notes_app/add-note.html')


def save_note(request):
    text = request.POST['note-text']
    if not text:
        return render(request, 'notes_app/add-note.html', {'is_empty': True})
    else:
        email = request.user.email
        new_note = Note(user_email=email, note_text=text, date=timezone.now())
        new_note.save()
        return redirect('index')


def all_notes(request):
    email = request.user.email
    notes_records = Note.objects.filter(user_email=email)
    return render(request, 'notes_app/all-notes.html', {'notes_records': notes_records})


def sign_out(request):
    logout(request)
    return redirect('index')
