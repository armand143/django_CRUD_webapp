from datetime import datetime
from email import message
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import superuser, posts
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.core.mail import send_mail
from django.contrib import messages

import re


# Create your views here.

# def home(request):
#     return HttpResponse("Welcome Stefan Jagemann")

def home(request):
    return render(request, 'homepage.html', {})


def addPost(request):
    form = postForm() #when browser reloaded, entered information appears again because we pass this into context
    context = {'form': form}
    if request.method == 'POST':
        form = postForm(request.POST or None, request.FILES)
        if form.is_valid:
            form.save()
        newestPost = posts.objects.filter(title=form.cleaned_data.get("title"))[0]
        newestPost.createdOn = str(datetime.now())[:10]
        #createdOnDate = str((datetime.now()).strftime("%Y-%m-%d"))
        newestPost.save()
        all_posts = posts.objects.all()
        posts_lib = {'lib': all_posts,
                    #   'c_date': creatDate
                    }

        return render(request, 'posts.html', posts_lib)
    else:
        return render(request, 'addPost.html', context)


def allPosts(request):
    all_posts = posts.objects.order_by('-createdOn')
    if mobile(request):
        is_mobile = True
    else:
        is_mobile = False

    all_posts_lib = {'lib': all_posts, 'is_mobile': is_mobile}
    return render(request, 'posts.html', all_posts_lib)


def tagesBuch(request):
    all_posts = posts.objects.order_by('-createdOn')
    if mobile(request):
        is_mobile = True
    else:
        is_mobile = False

    all_posts_lib = {'lib': all_posts, 'is_mobile': is_mobile}
    return render(request, 'tagesbuch.html', all_posts_lib)


def deletePost(request, p_id):
    dead_post = posts.objects.get(pk=p_id)
    dead_post.delete()
    return redirect('allPosts')


def editProfile(request):
    form = superuser(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid:
        form.save()
        return render(request, 'editProfile.html', {})
    else:
        return render(request, 'homepage.html', context)


def editPost(request, p_id):
    post = posts.objects.get(pk=p_id)
    edit_form = postForm(instance=post)
    context = {'form': edit_form}
    if request.method == "POST":
        edit_form = postForm(request.POST or None, request.FILES, instance=post)
        if edit_form.is_valid:  
            edit_form.save()
            contextt = {
                'all_posts': posts.objects.all(),

            }
            return redirect('allPosts')
    else:
        return render(request, 'editPost.html', context)


def editProfile(request):
    user_profile = request.user
    form = profileForm(request.POST or None, instance=user_profile)

    if request.method == "POST":
        form = profileForm(request.POST or None,
                           request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
        context = {'form': form, 'all_U': superuser.objects.all()}
        return render(request, 'editProfile.html', context)

    else:
        context = {'form': form, 'all_U': superuser.objects.all()}
        return render(request, 'editProfile.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    sent = False 
    context = {'form': form, 'pop_up': False}
    

    if request.method == "POST":
        vorname = request.POST.get('vorname')
        nachname = request.POST.get('nachname')
        email = request.POST.get('email')
        betreff = request.POST.get('betreff')
        nachricht = request.POST.get('nachricht')

        data = {
            'Betreff': betreff,
            'Email-Adresse' : email,
            'Vorname' : vorname ,
            'Nachname' : nachname,
            'Nachricht' : nachricht,
            
        }

        message = """ 
        Namen: {} {}

        Nachricht: {}

        From: {}
        """.format(data['Vorname'], data['Nachname'], data['Nachricht'], data['Email-Adresse'])
        send_mail(data['Betreff'], message, '', ['developmenttest31@gmail.com'])
        sent = True
        print(data)
        context = {'form': form, 'pop_up': True}
        
        messages.success(request, "erfolgreich gesendet")
        #return render(request, 'contact.html', context)

    return render(request, 'contact.html', context)

def therapieangebot(request):
    return render(request, 'therapieangebot.html', {})



def mobile(request):
# """Return True if the request comes from a mobile device."""
    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False

def impressum(request):
    return render(request, 'Impressum.html', {}) 