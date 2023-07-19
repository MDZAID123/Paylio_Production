from django.contrib import admin

# Register your models here.
from userauths.models import User
# we need to go ahead and register this also
#  we want to register the user 
admin.site.register(User)
