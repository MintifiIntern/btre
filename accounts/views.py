from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # messages.error(request, 'testing')
        # return redirect('register')

        # register user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #user and mail checking if already exist
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already in use')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already in use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                                                    username=username,email=email,password=password)
                    # auth.login(request, user)
                    # messages.success(request,'user logged in')
                    # return redirect('index')

                    user.save()
                    messages.success(request,'user is now registered')
                    return redirect('login')
        else:
            #password checking
            messages.error(request,'password does not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'user now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you are logged out')
        return redirect('login')
    else:
        return redirect('index')

def signup(request):
    return render('')



def dashboard(request):
    return render(request, 'accounts/dashboard.html')
