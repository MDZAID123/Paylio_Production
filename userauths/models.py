from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# now we are going to to create a custom user 
class User(AbstractUser):

    # class Meta:
    #     abstract = True
       
    #     app_label= 'userauths'
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']
    # now we will be creating a string representation of this object
    # 



    def __str__(self):
        return self.username
    
