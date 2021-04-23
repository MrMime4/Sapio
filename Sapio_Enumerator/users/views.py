from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from streamapp import views

def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
        user.save()
        request.session['id'] = user.id
        return redirect('/')
    else:
        return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        if (User.objects.filter(email=request.POST['login_email']).exists()):
            user = User.objects.filter(email=request.POST['login_email'])[0]
            if (request.POST['login_password'] == user.password):
                request.session['id'] = user.id
                return redirect('/successL')
        return redirect('/')

def successL(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'users/successL.html', context)