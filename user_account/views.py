from django.shortcuts import render
from .forms import CreateTaskForm

def create_task(request):
    
    return render(request, 'user_account/create_task.html', {
        'form':CreateTaskForm,
    })

def account(request):
    
    return render(request, 'user_account/account.html', {})