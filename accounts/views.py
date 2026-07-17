from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import LoginForm



# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f"Welcome Back {user.username}")
        return redirect('book_list')
    
    else:
        messages.error(request, "Invalid credentials")
    return (request, 'acccounts/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')
