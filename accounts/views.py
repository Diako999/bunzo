from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def register(request):
    return render(request, 'register.html')

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if username == " " and email == " " and password == " " and password2 == " ":
            messages.error(request, 'please fill up all the fields')
            return redirect('register')
        if User.objects.filter(username = username).exists():
            messages.error(request, 'username already exists choose another username please')
            return redirect('register')
        if User.objects.filter(email = email).exists():
            messages.error(request, 'a user already exists with this email')
            return redirect('register')
        if password == password2:
            user = User.objects.create_user(username = username, email = email)
            user.save()
            user = User.objects.get(username = username)
            user.set_password(password)
            user.save()
            messages.success(request, 'registeration successfull. you can log in, Enjoy:)')
            return redirect('index')
        else:
            messages.error(request, 'passwords are not match')
            return redirect('register')
