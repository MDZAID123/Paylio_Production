from account.models import Account
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect

# here we will be creating a new view 

from django.db.models import Q
from django.contrib import messages
from decimal import Decimal

from core.models import Transaction

#logic is that users should be logged in to use this page for searching other users




@login_required
def search_users_account_number(request):


    # account=Account.objects.filter(account_status="active")//this logic will be used and implemented later 
    #for now let us use all of them 
    account=Account.objects.all()

    #define the context variable 

    # to return users by account number we need to fetch what the user type in 
    # and that can be done using a post request 

    query=request.POST.get("account_number")
    # print(query)
    # we have addded the above statement for testing purposes only

    if query:
        account=account.filter(
        Q(account_number=query)|
        Q(account_id=query)
        ).distinct()


    context={
        "account":account,

        "query":query,
    }

    return  render(request,"transfer/search-user-by-account-number.html",context)




# creating a new view for account transfer


def AmountTransfer(request,account_number):


    try:
        account=Account.objects.get(account_number=account_number)
    except:
        # account=None
        messages.warning(request,"Account does not exist")
        return redirect("core:search-account")
    context={
        "account":account ,
    }

    return render(request,"transfer/amount-transfer.html",context)
# note that every specific view is associated with a url 





def AmountTransferProcess(request,account_number):
    account=Account.objects.get(account_number=account_number) ## this will get the user that the currently logged in user wants money to send to 
    sender=request.user # the person that is logged in 
    # note that we will be getting all these details from the transaction model instantiation
    receiver=account.user
    sender_account=request.user.account
    receiver_account=account 

    if request.method=="POST":
        amount=request.POST.get("amount-send")
        description=request.POST.get("description")
        print(amount)
        print(description)

        # we also did put check on the frontend using javascript but smart guys can change that using inspect
        #element
        # so it is a good practice to keep track while on the serveri

        if sender_account.account_balance>= Decimal(amount):
            new_transaction=Transaction.objects.create(
                user=request.user,
                amount=amount,
                description=description,
                receiver=receiver,
                sender=sender,
                sender_account=sender_account,
                receiver_account=receiver_account,
                status="processing",
                transaction_type="transfer"

            )
            new_transaction.save()
            # save the transaction id 
            #redirect the user to the new page
            # getr the id of the newly created transaction
            transaction_id=new_transaction.transaction_id

            # the transfer confirmation page will be inheriting from
            # transaction
            return redirect("core:transfer-confirmation",account.account_number,transaction_id)
        
        else:
            messages.warning(request,"Insufficient Balance")
            return redirect("core:amount-transfer",account_number)
    else:
        messages.warning(request,"Error occured try again")
        return redirect("account:account")
    


def TransferConfirmation(request,account_number,transaction_id):

    try:
        account=Account.objects.get(account_number=account_number)
        transaction=Transaction.objects.get(transaction_id=transaction_id)
        
    except:
        messages.warning(request,"transaction does not exist")
        return redirect("account:account")
    context={
        "account":account,
        "transaction":transaction
    }
    return render(request,"transfer/transfer-confirmation.html",context)



# now creating a new view for final review process

def TransferProcess(request,account_number,transaction_id):
    # here the account number is the account of the number that basically want to intiate the payment process
    account=Account.objects.get(account_number=account_number)
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    sender=request.user
    receiver=account.user
    sender_account=request.user.account
    receiver_account=account
    completed=False

    if request.method=="POST":
        # first grab the pin number 
        pin_number=request.POST.get("pin-number")
        print(pin_number)


        if pin_number==sender_account.pin_number:
            # after validating the pin number just make the transaction completed 
            # and release the cash into receiver account
            transaction.status="completed"
            transaction.save()
            # remove the amount 
            sender_account.account_balance-=transaction.amount
            sender_account.save()
            #add the amount that was removed from my account to receiver account

            account.account_balance+=transaction.amount
            account.save()
            # here in this function  based view 
            # account_number is the one to which we are trying to send money to 

            messages.success(request,"Payment successful")
            # after the transaction is completed succesfully 
            # redirect the user to the completed successsfully page

            return redirect("core:transfer-completed",account.account_number,transaction.transaction_id)
        
        else:
            messages.warning(request,"Incorrect Pin")
            return redirect('core:transfer-confirmation',account.account_number,transaction.transaction_id)

    else:
        messages.warning(request,"An error occured plz try again later.")
        return redirect('account:account'  )



# creating a new view for transfer successfull page


def TransferCompleted(request,account_number,transaction_id):

    try:
        account=Account.objects.get(account_number=account_number)
        transaction=Transaction.objects.get(transaction_id=transaction_id)
        
    except:
        messages.warning(request,"transaction does not exist")
        return redirect("account:account")
    context={
        "account":account,
        "transaction":transaction
    }
    return render(request,"transfer/transfer-completed.html",context)

