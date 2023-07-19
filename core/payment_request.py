from account.models import Account
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect

# here we will be creating a new view 

from django.db.models import Q
from django.contrib import messages
from decimal import Decimal

from core.models import Transaction
from decimal import Decimal

# logic is that for making payment request we  should have login decorator over the view that we will making

@login_required
def SearchUsersRequest(request):
    account=Account.objects.all()

    query=request.POST.get("account_number")


    if query:
        account=account.filter(
            Q(account_number=query)|
            Q(account_id=query)
        ).distinct()


    context={
        "account":account,
        "query":query,


    }
    return render(request,"payment_request/search-users.html",context)




# NOW WE WILL be creating  a view that weill take after redirect from choose from request a payment page 
def AmountRequest(request,account_number):
    account=Account.objects.get(account_number=account_number)

    context={
        "account":account,
    }

    return render(request,"payment_request/amount-request.html",context)




def AmountRequestProcess(request,account_number):
    account=Account.objects.get(account_number=account_number)
    sender=request.user # who is the user is intiating  a payment request 
    receiver=account.user 
    # sender who is sendind payment request 
    #  reeiver who will be recieving payment request


    sender_account=request.user.account;
    receiver_account=account;

    if request.method=="POST":
        amount=request.POST.get("amount-request")
        description=request.POST.get("description")
        new_request=Transaction.objects.create(
            user=request.user,
            amount=amount,
            description=description,
            sender=sender,
            receiver=receiver,
            sender_account=sender_account,
            receiver_account=receiver_account,
            status="request_processing",
            transaction_type="request",


        )
        new_request.save()
        transaction_id=new_request.transaction_id
        return redirect("core:amount-request-confirmation",account.account_number,transaction_id)
    
    else:
        messages.warning(request,"error occured try again later!")
        return redirect("account:dashboard")




def AmountRequestConfirmation(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    context={
        "account":account,
        "transaction":transaction,
    }
    return render(request,"payment_request/amount-request-confirmation.html",context)




def AmountRequestFinalProcess(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)


    if request.method =='POST':
        pin_number=request.POST.get("pin-number")
        if pin_number==request.user.account.pin_number:
            transaction.status="request_sent"
            transaction.save()
            messages.success(request,"Your payment request has been sent successfully")
            return redirect("core:amount-request-completed",account.account_number,transaction.transaction_id)
        


    else:
        messages.warning(request,"An Error Occured ,Try again later ")
        return redirect("account:dashboard")
    


def RequestCompleted(request,account_number,transaction_id):
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    account=Account.objects.get(account_number=account_number)
    context={
        "account":account,
        "transaction":transaction,
    }
    return render(request,"payment_request/amount-request-completed.html",context)




#  ##################### payment settlement views from here specifically 
def settlement_confirmation(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    context={
        "account":account,
        "transaction":transaction,
    }
    return render(request,"payment_request/settlement-confirmation.html",context)
#view -url -template create karte h





def settlement_processing(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    sender=request.user # this sender is logged in user which is seeing his request and settleing them 
    sender_account=request.user.account

    if request.method=="POST":
        pin_number=request.POST.get("pin-number")
        if pin_number == request.user.account.pin_number:
            if sender_account.account_balance<=0 or sender_account.account_balance<transaction.amount:
                messages.warning(request,"insufficient funds,fund your account and try again .")

            else:
                # if i have enough funds to settle them 
                # then i have 2 choices either i can  settle the request  or simple delete it '
                sender_account.account_balance-=transaction.amount
                # in django after we have updated any model object
                sender_account.save()
                #  now just load the cash into requested persons account
                account.account_balance+=transaction.amount 
                account.save()
                transaction.status="request_settled"
                transaction.save()


                messages.success(request,f"Settled to {{ account.user.kyc.full_name }} was successful")
                return redirect("core:settlement-completed",account.account.account_number,transaction.transaction_id)
        else:
            messages.warning(request,"Incorrect Pin")
            return redirect("core:settlement-confirmation",account.account_number,transaction.transaction_id)
        
    else:
        messages.warning(request,"Error Occured")
        return redirect("account:settlement")
    

# another view for settlement completed page 


def SettlementCompleted(request,account_number,transaction_id):
    account=Account.objects.get(acount_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)


    context={
        "account":account,
        "transaction":transaction,

    }
    return render(request,"payment_request/settlement-completed.html",context)

    


# new view for deleting payment request  that not settled till now by sender
def deletePaymentRequest(request,account_number,transaction_id):
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
   

    # we need to make sure that the person deleting this transaction is actually the person who raised it 


    if request.user == transaction.user:
        transaction.delete()
        messages.success(request,"Payment request Deleted Successfully")
        return redirect("core:transactions")
    
    # return render(request,"payment_request/delete-payment-request.html",context)

    