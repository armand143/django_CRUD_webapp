from re import template
from django.http import request
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistrationForm

# class Registration(generic.CreateView):
#     form_class = RegistrationForm(request.POST)
#     template_name = 'registration/register.html'
#     done_url = reverse_lazy('login')


def registration(request):
    form = RegistrationForm()

    if request.method == 'POST' and form.is_valid():
        form = RegistrationForm(request.POST)
        form.save()

        return redirect('login')
    
    context = {'form': form}
    return render(request, "registration/register.html", context)

#def loginPage(request):














# Create your views here.
