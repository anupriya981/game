from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import customer

# Create your views here.
def show_account(request):

    context={}
    if request.method == 'POST' and 'Register' in request.POST:
        context['Register'] = True
        try:

            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            age = request.POST.get('age')

                # create user account

            user = User.objects.create_user(
                    username=username,
                    password=password,
                    # conform_password=conform_password,
                    email=email
                )

                # create customer account
            Customer = customer.objects.create(
                    user=user,
                    age=age,
                    phone=phone
                ) 
            # return redirect('home')  
            success_message="Sign-up successful! You can now log in."
            messages.success(request, success_message)
            return redirect ('login')
        except Exception as e:
         error_message = "An error occurred during registration. Please try again later."
         messages.error(request, error_message)
    
    return render(request, 'account.html')



def user_login(request):
    context={}
    if request.method == 'POST' and 'login' in request.POST: 
        context['Register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')  
    return render(request, 'login.html', context)



def sign_out(request):
    logout(request)
    return redirect('home')

