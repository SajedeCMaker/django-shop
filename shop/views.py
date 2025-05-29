from django.shortcuts import render , redirect
from . models import Product 
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import signup_form

def shop(request):
    all_products = Product.objects.all()
    return render(request ,'index.html', {'products':all_products})
def about(request):
    return render(request ,'about.html')

def login_user(request):
    if request.method == "POST" :
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        remember = request.POST.get('remember_me')
        user = authenticate(request , username = 
                             username , password = password)
        
        if user is not None:
            if remember:
                request.session.set_expiry(1209600) 
            else:
                request.session.set_expiry(0)
            login(request, user)
            messages.success(request,'با موفقیت وارد شدید')
            return redirect("shop")
        else :
            messages.error(request,'مشکلی در لاگین شدن وجود داشت')
            return redirect("login")

    else :
        return render(request ,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request , 
                     'با موفیقت خارج شدید')
    return redirect("shop")

def signup_user(request):
    form = signup_form()
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request , username=username , password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'اکانت شما ساخته شد')
                return redirect("shop")
        else:
            messages.error(request, form.errors)
            return redirect("signup")
            
    return render(request ,'signup.html', {'form': form})
    
def product(request , pk):
    product = Product.objects.get(id=pk)
    return render(request ,'product.html', {'product':product})