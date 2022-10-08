from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, "Başarıyla Kayıt Oldunuz...")

        return redirect("dashboard")
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "accounts/login.html", context)

        messages.success(request, "Başarıyla Giriş Yaptınız")
        login(request, user)
        return redirect("dashboard")
    return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yaptınız")
    return redirect("index")


def forgot(request):
    return render(request, "accounts/forgot.html")


def reset(request):
    return render(request, "accounts/reset.html")