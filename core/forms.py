from django import forms

from core.models import CreditCard


class CreditCardForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Card Holder Name"}))
    number=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Card Number"}))
    month=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"exipiry Month"}))
    year=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"expiriy field"}))
    cvv=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"CVV"}))


    class Meta:
        model=CreditCard
        fields=['name','number','month','year','cvv','card_type']


 