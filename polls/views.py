from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def counter(request):
    text = request.POST['text_form']
    context = {
        'characters': len(text),
        'words': len(text.split())
    }
    return render(request, 'counter.html', context)


def register(request):
    if request.method == 'post':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'post':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})


def posts(request):
    posts = [1, 2, 3, 4, 5, 'test', 'tests', 'testing']
    return render(request, 'counter.html', {'posts': posts})
