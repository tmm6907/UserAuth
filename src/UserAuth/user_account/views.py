from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import Secret
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_account:secret-page')
        else:
            messages.info(request, "Login failure")
    return render(request,'user_account/login.html', context={})
    

def signup_page_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('user_account:login-page')
    context={'form':form}
    return render(request,'user_account/signup.html', context)

def secret_view(request):
    print(request.user)
    obj = Secret.objects.filter(username = request.user)
    return render(request,'user_account/secret.html',context={'object':obj})