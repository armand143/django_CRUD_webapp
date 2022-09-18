from datetime import datetime
from email import message
from turtle import title
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import superuser, posts
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.core.mail import send_mail


# Create your views here.

# def home(request):
#     return HttpResponse("Welcome Stefan Jagemann")

def home(request):
    return render(request, 'homepage.html', {})


def addPost(request):
    form = postForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid:
        form.save()
        newestPost = posts.objects.filter(title=request.POST['title'])[0]
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
    all_posts_lib = {'lib': all_posts}
    return render(request, 'posts.html', all_posts_lib)


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
    edit_form = postForm(request.POST or None, instance=post)
    context = {'form': edit_form}
    if request.method == "POST" and edit_form.is_valid:
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
    context = {'form': form}

    if request.method == "POST":
        vorname = request.POST.get('vorname')
        nachname = request.POST.get('nachname')
        email = request.POST.get('email')
        betreff = request.POST.get('betreff')
        nachricht = request.POST.get('nachricht')

        data = {
            'Betreff': betreff,
            'Email-Adresse' : email,
            'Name' : vorname ,
            'Nachricht' : nachricht,
            
        }

        message = """ 
        New message: {}

        From: {}
        """.format(data['Nachricht'], data['Email-Adresse'])
        send_mail(data['Betreff'], message, '', ['developmenttest31@gmail.com'])
        print(data)

    return render(request, 'contact.html', context)
