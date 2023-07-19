from django import forms
from account.models import KYC
from django.forms import ImageField,FileInput,DateInput



class DateInput(forms.DateInput):

    input_type='date'


class KYCForm(forms.ModelForm):
    identity_image=ImageField(widget=FileInput)
    image=ImageField(widget=FileInput)
    signature=ImageField(widget=FileInput)


    class Meta:
        model=KYC

        fields=[
            'full_name',
            'image',
            'marrital_status',
            'gender',
            'identity_type',
            'identity_image',
            'date_of_birth',
            'signature',
            'country',
            'state',
            'city',
            'mobile',
            'fax',
        ]
        # we can also put initial placeholder
        widgets={
            "full_name":forms.TextInput(
                attrs={
                    "placeholder":"Full Name",
                    "class":"",
                    "id":"",
                }
            ),
            "mobile":forms.TextInput(
                attrs={
                    "placeholder":"Mobile Number",
                    "class":"",
                    "id":"",
                }
            ),
            "fax":forms.TextInput(
                attrs={
                    "placeholder":"Fax Number",
                    "class":"",
                    "id":"",
                }
            ),
            "country":forms.TextInput(
                attrs={
                    "placeholder":"Country",
                    
                }
            ),
            "state":forms.TextInput(
                attrs={
                    "placeholder":"state",
                    "class":"",
                    "id":"",
                }
            ),
            'date_of_birth':DateInput,
            "city":forms.TextInput(
                attrs={
                    "placeholder":"city",
                    "class":"",
                    "id":"",
                }
            ),
         
          
          
        }