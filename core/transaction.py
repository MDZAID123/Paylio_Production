from core.models  import Transaction 
from django.shortcuts  import render,redirect
from account.models import Account
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# here we will be creating a function based view for transaction list


@login_required
def transaction_lists(request):
    sender_transaction=Transaction.objects.filter(sender=request.user,transaction_type="transfer").order_by("-id")
    receiver_transaction=Transaction.objects.filter(receiver=request.user,transaction_type="transfer").order_by("-id")

    request_sender_transaction=Transaction.objects.filter(sender=request.user,transaction_type="request") # this will contain all the payment request that we send to other persons
    request_receiver_transaction=Transaction.objects.filter(receiver=request.user,transaction_type="request") # this will contain all the payment request that we are receiving from other people

    # we are ordering them by id to put the latest on on the top 
    #here we are trying to list down all the transactions intiated by all of them 
    context={
        "sender_transaction":sender_transaction,
        "receiver_transaction":receiver_transaction,
        "request_sender_transaction":request_sender_transaction,
        "request_receiver_transaction":request_receiver_transaction
    }

    return render(request,"transaction/transaction-list.html",context)


# in django you can make certain view  login required 

@login_required
def transaction_detail(request,transaction_id):
    transaction=Transaction.objects.get(transaction_id=transaction_id)
    # receiver_transaction=Transaction.objects.filter(receiver=request.user).("-id")
    # we are ordering them by id to put the latest on on the top 
    #here we are trying to list down all the transactions intiated by all of them 
    c={
        "transaction":transaction,
    }

    return render(request,"transaction/transaction-detail.html",c)






