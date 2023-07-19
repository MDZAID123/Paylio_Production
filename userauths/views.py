from django.shortcuts import render,redirect

from userauths.forms import UserRegisterForm

from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages

from userauths.forms import UserRegisterForm
from userauths.models import User
# the above is going to show a flash message like account created

# note that render will not work if we pass the context in it as an argument

def RegisterView(request):


    if request.method == 'POST':

        form=   UserRegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save() 
            email=form.cleaned_data.get("email")
            username=form.cleaned_data.get("username")
            # there are lot of ways to do the same thing
            #username=request.POST.get("username")
            messages.success(request,f"hey {username} ,your account was created successfully")
            new_user=authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])



            login(request,new_user)
            return redirect("account:account")


            # form.save()

    

    if request.user.is_authenticated:
        messages.warning(request,f"You are already logged in ")
        return redirect("account:account")
    else:
        form=UserRegisterForm()

    context={
        "form":form
    }
    return render(request,"userauths/sign-up.html",context)

def logoutView(request):
    logout(request)
    messages.success(request,"you have been logged out")
    return redirect("userauths:sign-in")



def LoginView(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")


        try:
            user=User.objects.get(email=email)
            user=authenticate(request,email=email,password=password)

            # if  user does not exists

            if user is not None:
                login(request,user)
                messages.success(request,"Your are logged")
                # if they are successfully logged in 
                # then redirect them to the home page
                return redirect("account:account")
            
            else:
                messages.warning(request,"username or password does not exist")
                return redirect("userauths:sign:in")
            

        
            
        except:
            messages.warning(request,"User does not exist")

    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect("account:account")
    return render(request,"userauths/sign-in.html")