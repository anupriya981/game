from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import register
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Dest_img
from .models import Destination_details
from .models import Travellers
from .models import VisitPlace
from django.contrib import auth

# Create your views here.

def Home(request):
    backgro_img=Dest_img.objects.all()
    detail=Destination_details.objects.all()
    travel=Travellers.objects.all()
    context={'bg_img':backgro_img ,'details':detail ,'travels':travel}

    return render(request, 'home.html' ,context)

def Register(request):
    if request.method== 'POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        confirm_pass=request.POST['confirm_pass']
        email=request.POST['email']
        if password==confirm_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username_taken')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
                return redirect('registration')
            else:
                user=User.objects.create_user(
                    # name=name,
                    username=username,
                    password=password,
                    email=email
                    # confirm_pass=confirm_pass
                )
                user.save()
                print('user_created')
                return redirect('login')
        else:
            messages.info(request, 'password is not maching..')
            return redirect('registration')
    return render(request, 'registration.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credential')
            return redirect(request, "login")
    else:
        return render(request, 'login.html')
    
def Logout(request):
    auth.logout(request)
    return redirect("/")

def Tra_des(request,pk):
    instance = Destination_details.objects.get(pk=pk)
    instance2 = VisitPlace.objects.all()
    return render(request, 'traveler_descri.html', {'instane':instance, 'instane2':instance2})

def Place_descri(request,pk):
    instance = VisitPlace.objects.get(pk=pk)
    return render(request, 'place_descri.html', {'instane':instance})

# def Page(request):
#     instance = VisitPlace.objects.all()
#     return render(request, 'page.html',{'instane':instance})
