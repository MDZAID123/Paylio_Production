from django.db import models

from userauths.models import User
from account.models import Account


from shortuuid.django_fields import ShortUUIDField
# Create your models here.


TRANSACTION_TYPE=(

    ("transfer","Transfer"),
    ("received","Received"),
    ("withdraw","Withdraw"),
    ("refund","Refund"),
    ("request","Payment Request"),
    ("none","None"),
)
TRANSACTION_STATUS=(
    ("failed","failed"),
    ("completed","completed"),
    ("pending","pending"),
    ("processing","processing"),
    ("request_sent","request_sent"),
    ("request_settled","request_settled"),
    ("request_processing","request_processing"),
)


CARD_TYPE=(
    ("master","master"),
    ("visa","visa"),
    ("verve","verve"),
)
class Transaction(models.Model):
    # every transaction should have a unique transaction id
    transaction_id=ShortUUIDField(unique=True,length=15,max_length=20,prefix="TRN")
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True ,related_name="user")
    amount=models.DecimalField(max_digits=12,decimal_places=2,default=0.00)



    description=models.CharField(max_length=1000,null=True,blank=True)

    # We Dont want to do anything when the user that owns the transaction gets deleted because still
    # because for security purposes we still want to keep record of it in our database
    receiver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True, related_name="receiver")
    sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True , related_name="sender")

    receiver_account=models.ForeignKey(Account,on_delete=models.SET_NULL,null=True , related_name="receiver_account")
    sender_account=models.ForeignKey(Account,on_delete=models.SET_NULL,null=True , related_name="sender_account")

    # by logic a transaction should have a unique status at a time 
    # either it should be pending succedd fail
    status=models.CharField(choices=TRANSACTION_STATUS,max_length=100,default="pending")
    transaction_type=models.CharField(choices=TRANSACTION_TYPE,max_length=100,default="none")
    # time should also be associated as an atrribute to a particular transaction
    
    date=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=False,null=True,blank=True)



    def __str__(self):
        try:
            return f"{self.user}"
        except:
            return f"Transaction"
        


# models.CASCAde MEANS THAT if the associate user with that featue let say credit card is deleted 
# then the corresponding credit card is also deleted 


class CreditCard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    card_id=ShortUUIDField(unique=True,length=5,max_length=20,prefix="CARD",alphabet="1234567890")
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    month=models.IntegerField()
    year=models.IntegerField()
    cvv=models.IntegerField()

    amount=models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    card_type=models.CharField(choices=CARD_TYPE,max_length=20,default="master")
    card_status=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)

    # now let us define a string representation of the object 

    def __str__(self):
        return f"{self.user}"
    



