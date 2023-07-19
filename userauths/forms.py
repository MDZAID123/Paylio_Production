# forms to create account for user
from django import forms

from django.contrib.auth.forms import UserCreationForm



from userauths.models import User


class UserRegisterForm(UserCreationForm):
    # make sure that this class extends from usercreation form
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
