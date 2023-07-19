from decimal import Decimal
from django.shortcuts import render,redirect 

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from core.models import CreditCard
from decimal import Decimal
from account.models import Account


def card_detail(request,card_id):
    credit_card=CreditCard.objects.get(card_id=card_id,user=request.user)
    # let us go and also grab user's account
    account=Account.objects.get(user=request.user)

    context={
        "account":account,
        "credit_card":credit_card,
    }
    

    return render(request,"credit_card/card-detail.html",context)




# funding  our credit card 

def fund_credit_card(request,card_id):
    credit_card=CreditCard.objects.get(card_id=card_id,user=request.user)

    account=request.user.account

    if request.method=="POST":
        amount=request.POST.get("funding_amount")


        if Decimal(amount)<=account.account_balance:
            account.account_balance-=Decimal(amount)
            account.save()


            credit_card.amount+=Decimal(amount)
            credit_card.save()



            messages.success(request,"Funding Successful")
            return redirect("core:card-detail",credit_card.card_id)
        else:
            messages.warning(request,"Insufficent balance in your account")
            return redirect("core:card-detail",credit_card.card_id)
        


# withdraw funds from credit card 


def withdraw_fund(request,card_id):
    account=Account.objects.get(user=request.user)
    credit_card=CreditCard.objects.get(card_id=card_id,user=request.user)


    if request.method =="POST":
        amount=request.POST.get("amount")
        print(amount)

        if credit_card.amount >= Decimal(amount):
            account.account_balance+=Decimal(amount)
            account.save()
            credit_card.amount-=Decimal(amount)
            credit_card.save()


            messages.success(request,"Withdrawal successfull")
            return redirect("core:card-detail",credit_card.card_id)
        else:
            messages.warning(request,"Insufficient fund in your credit card")
            return redirect("core:card-detail",credit_card.card_id)
        


def  delete_card(request,card_id):
    credit_card=CreditCard.objects.get(card_id=card_id,user=request.user)

    credit_card.delete()

    messages.success(request,"Card Delete successfull")
    return redirect("account:dashboard")
