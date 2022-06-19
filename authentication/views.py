from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from authentication.register_form import SignUpForm
from authentication.login_form import LoginForm


def index(request):
    return render(request, "select.html")


def register(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        form.save()

        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
        return redirect('/')

    return render(request, "register.html", {'form': form})


def log_in(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, "login.html", {'form': form})


def log_out(request):
    logout(request)
    return redirect("/")
