from django.contrib import admin

# Register your models here.
# we need register our app specific models into our app specific admin files
from core.models import Transaction,CreditCard


# whenever we create a new model we need to register the same in our admin file
class TransactionAdmin(admin.ModelAdmin):
    list_editable=['amount','status','transaction_type','receiver','sender']
    list_display=['user','amount','status','transaction_type','receiver','sender']


class CreditCardAdmin(admin.ModelAdmin):
    list_editable=['amount','card_type']
    list_display=['user','amount','card_type']

admin.site.register(Transaction,TransactionAdmin)
admin.site.register(CreditCard,CreditCardAdmin)

