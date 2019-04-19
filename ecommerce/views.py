from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'title': 'Home',
        'content': 'this is the home page',

    }
    if (request.user.is_authenticated()):
        context['premium_content']='YEAHHHHHHHH!'
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'title': 'About',
        'content': 'this is the about page'
    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'this is the contact page',
        'form': contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print("User logged in : {}".format(request.user.is_authenticated()))
    if form.is_valid() :
        print("data : {}".format(form.cleaned_data))
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['form'] = form
            return redirect("/")


        else:
            print("ERROR!")




    return render(request, "auth/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.changed_data)
    return render(request, "auth/register.html", context)
