from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def login_page(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect("/recipes/")  # Redirect if already logged in

    form = AuthenticationForm()
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect("/recipes/")  # Redirect to homepage or dashboard
        else:
            messages.error(req, "Invalid username or password.")

    return render(req, 'users/login.html', {"form": form})

def register_page(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect("/recipes/")  # Redirect if already logged in

    form = UserCreationForm()
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)  # Log in the user after registration
            messages.success(req, "Registration successful! Welcome.")
            return redirect("/recipes/")  # Redirect to homepage or dashboard
    return render(req, 'users/register.html', {"form": form})

def logout_route(req : HttpRequest):
    if req.method == 'POST':
        logout(req)
        return redirect('/')