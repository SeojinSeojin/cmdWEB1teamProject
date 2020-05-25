from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .models import User
from . import forms


def log_in(request):
    if request.method == "GET":
        form = forms.LoginForm
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            studentID = form.cleaned_data.get("studentID")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=User.objects.get(
                studentID=studentID).username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("main"))
        return render(request, "login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("main"))


def sign_up(request):
    if request.method == "GET":
        form = forms.SignUpForm
        return render(request, "signup.html", {"form": form})
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect(reverse("main"))
    return render(request, "signup.html", {"form": form})
