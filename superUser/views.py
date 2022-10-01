from re import template
from django.http import request
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import LoginForm, RegistrationForm
from django.contrib import messages

# class Registration(generic.CreateView):
#     form_class = RegistrationForm(request.POST)
#     template_name = 'registration/register.html'
#     done_url = reverse_lazy('login')


def registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Dein Passwort muss mindestens 8 Zeichen enthalten.")
            messages.error(request, "Die Passwörter müssen übereinstimmen")

    context = {'form': form}
    return render(request, "registration/register.html", context)


def log_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if username == 'admin':
                return redirect('allPosts')
            else:
                return redirect('homepage')
        else:
            messages.error(request, "Name oder Passwort ist falsch.")
    # return redirect('login')
    context = {'form': form}
    return render(request, "registration/login.html", context)


# def loginPage(request):














# Create your views here.
