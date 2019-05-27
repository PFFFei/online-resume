from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from .models import User

def home(request):
    return render(request,'accounts/home.html')

def resume(request):
	return render(request,'accounts/resume.html')

def login_view(request):  # users will login with their Email & Password
    if request.user.is_authenticated:
        return redirect("accounts:home")
    else:
        title = "登 陆"
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            # authenticates Email & Password
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("accounts:home")
        context = {"form": form,
                   "title": title
                   }

        return render(request, "accounts/form.html", context)


def register_view(request):  # Creates a New Account & login New users
    if request.user.is_authenticated:
        return redirect("accounts:home")
    else:
        title = "注 册"
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)
            return redirect("accounts:home")

        context = {"title": title, "form": form}

        return render(request, "accounts/form.html", context)


def logout_view(request):  # logs out the logged in users
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    else:
        logout(request)
        return redirect("accounts:home")
