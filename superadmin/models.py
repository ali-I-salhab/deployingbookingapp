from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


     

# Create your models here.



class Hotel(models.Model):
    name = models.CharField(max_length=255)
    country = models.TextField()
    city = models.TextField(null=True, blank=True)
    phonenumber=models.TextField()


    # phonenumber = models.DecimalField(
    #     max_digits=6,
    #     decimal_places=2,
    #     validators=[MinValueValidator(1)])
    Googlereviewnumber = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    website = models.TextField(null=True, blank=True)
    email =  models.TextField(null=True, blank=True)

    facebookaccount = models.TextField(null=True, blank=True)

    verticalline = models.TextField(null=True, blank=True)
    horizontalline = models.TextField(null=True, blank=True)


    # here we get only title for Product object wheen we make Query set
    # without it give us list of products as objects return self
   

    # def __str__(self) -> str:
    #     return self.title

    # class Meta:
    #     ordering = ['title']

class HotelImages(models.Model):
    Hotel=models.ForeignKey(Hotel,related_name='uploaded_images',on_delete=models.CASCADE)     
    image=models.ImageField(upload_to='hotel/images',blank=True,null=True)   