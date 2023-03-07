from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login as cookies_login
from django.contrib import messages
from .models import CustomUser


def authenticate_user(request):
    user = authenticate(request,
        username = request.POST.get('email', ''),
        password = request.POST.get('password', '')
    )
    print(request.POST.get('email', ''))
    return user

def exists_email(email):
    exists = CustomUser.objects.filter(email=email).exists()
    return exists

# Views project
def home_page(request):
    return render(request, 'base/index.html', {})

def login(request):
    if request.method == 'get':
        return render(request, 'registration/login.html', {
            'form':LoginForm,
        })
    else:
        if authenticate_user(request) is None:
            return render(request, 'registration/login.html', {
                'form':LoginForm(request.POST),
            })
        return redirect('create_task')
            
def signup(request):
    if request.method == 'get':
        return render(request, 'home_page/signup.html', {
            'form':UserRegisterForm,
        })
    else:
        if UserRegisterForm(request.POST).is_valid():
            email = request.POST.get('email', '').lower()
            username = request.POST.get('username', '').lower()
            password = request.POST.get('password', '')
            # Register user
            if not exists_email(email):
                user = CustomUser.objects.create_user(
                    email=email,
                    username=username,
                    password=password,
                )
                user.save()
                cookies_login(request, user, backend='home_page.backends.CaseInsensitiveModelBackend')
                return redirect('create_task')
        return render(request, 'home_page/signup.html', {
            'form':UserRegisterForm(request.POST),
        }) 



