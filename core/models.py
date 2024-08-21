from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractUser):
    email = models.EmailField( unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    username=models.CharField(max_length=255,default='')
    country=models.CharField(max_length=255,default='a')
    phone= models.CharField(max_length=255,default='a')

    # # pass
    #     # username_validator = UnicodeUsernameValidator()
    #     REQUIRED_FIELDS = ['email']
     
    #     USERNAME_FIELD = 'email'
    #     email = models.EmailField(("email address"), unique=True)



    #     username = models.CharField(
    #     ("username"),
    #     max_length=150,
    #     unique=False,
    #     help_text=(
    #         "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    #     ),)
    
    

# Create your models here.
