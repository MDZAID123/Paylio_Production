from django.shortcuts import render ,redirect
from account.models import KYC,Account
from account.forms import KYCForm
from django.contrib import messages

from core.forms import CreditCardForm

from core.models import CreditCard

from django.contrib.auth.decorators import login_required

# @login_required
# there are other ways to achive the same logic
def account(request):

    if request.user.is_authenticated:



        try:
            kyc=KYC.objects.get(user=request.user)
        except:
            messages.warning(request,"You need to submit your kyc")
            return  redirect("account:kyc-reg")
        # here the above code has a logical error 
        # if the user is not authenticated ie that means usr has not submitted the kyc 
        # in that case redirect the user to that page 
    # logic is that only if the user has not submittted thekyc yet in that case just redirect the user 
    # note that projects will make impact on your resume


    else:
        messages.warning(request,"You need to login to access the dashboard")
        return redirect("userauths:sign-in")

    account=Account.objects.get(user=request.user)

    context={
        "kyc":kyc,
        "account":account,
    }
    

    return render(request,"account/account.html",context)

@login_required
def kyc_registration(request):
    # here we are defining a function based view for kyc regisrtration 
    user=request.user
    account=Account.objects.get(user=user)



    try:
        kyc=KYC.obects.get(user=user)
        # try to get the already exisiting kyc value with the user s
        # if exists
    except:
        kyc=None
    

    if request.method== "POST":

        form=KYCForm(request.POST,request.FILES,instance=kyc)
        # request.POST-will grab all the input fields 
        # first we will do verification then we will do that 
        if form.is_valid():
            # commit-FALSE does not directly save the kyc in the backend 
            new_form=form.save(commit=False)
            new_form.user=user
            # we need to dynamically populate some of the fields
            new_form.account=account
            new_form.save()
            messages.success(request,"KYC Form submitted successfully , In review now")
            return redirect("core:index")
        
    else:
        form=KYCForm(instance=kyc)

    context={
        "account":account,
        "form":form,
        "kyc":kyc,
    }
    return render(request,"account/kyc-form.html",context)



def dashboard(request):

    if request.user.is_authenticated:



        try:
            kyc=KYC.objects.get(user=request.user)
        except:
            messages.warning(request,"You need to submit your kyc")
            return  redirect("account:kyc-reg")
        # here the above code has a logical error 
        # if the user is not authenticated ie that means usr has not submitted the kyc 
        # in that case redirect the user to that page 
    # logic is that only if the user has not submittted thekyc yet in that case just redirect the user 
    # note that projects will make impact on your resume


        account=Account.objects.get(user=request.user)
        # get all the credit card of the user that is currently logged in 
        credit_card=CreditCard.objects.filter(user=request.user).order_by("-id")




        if request.method=="POST":
            form=CreditCardForm(request.POST)
            if form.is_valid():
                new_form=form.save(commit=False)
                new_form.user=request.user
                new_form.save()

                card_id=new_form.card_id

                messages.success(request,"Card Added Successfully")
                return redirect("account:dashboard")
        else:
            form=CreditCardForm()


    else:
        messages.warning(request,"You need to login to access the dashboard")
        return redirect("userauths:sign-in")


    context={
        "kyc":kyc,
        "account":account,
        "form":form,
        "credit_card":credit_card,
    }
    

    return render(request,"account/dashboard.html",context)

