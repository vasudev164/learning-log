from django.shortcuts import render
from .forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'users/index.html')


def signup(request):
    user_form = CreateUserForm()
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {
        'user_form': user_form,
    }
    return render(request, 'users/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
        else:
            return render(request, "users/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})
