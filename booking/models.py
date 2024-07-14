from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
# Create your models here.

# hotels
class Hotel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    namear = models.CharField(max_length=255,null=True,blank=True)
    nameen = models.CharField(max_length=255,null=True,blank=True)
    logo=models.ImageField(upload_to='hotel/logos',blank=True,null=True)
    Category = models.CharField(max_length=255,null=True,blank=True)
    HoteStars = models.SmallIntegerField(null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    postcode = models.CharField(max_length=255,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    long=models.FloatField(null=True,blank=True)
    descar=models.TextField(null=True,blank=True)
    descen=models.TextField(null=True,blank=True)
    policyen=models.TextField(null=True,blank=True)
    policyar=models.TextField(null=True,blank=True)
    icons=models.CharField(max_length=25,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        print('save')
        print(kwargs)
        
        super(Hotel, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.namear
    class Meta:
        ordering=['namear']
# Groups
# null in field makeit nullable in database level
# blank in field make it nullable in admin site
class Groups(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    currency=models.CharField(max_length=255)
    status=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

class GroupCountries(models.Model):
    name=models.CharField(max_length=255)
    group=models.ForeignKey(Groups,on_delete=models.CASCADE,related_name='countries')
# mealplans
class MealPlan(models.Model):
    
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)

    nameen=models.CharField(max_length=255)
    namear=models.CharField(max_length=255)
    descar=models.TextField()
    descen=models.TextField()
# photos




class Photos(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    phototype=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='hotel/photos')

# rooms
class Room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)

    namear = models.CharField(max_length=255)
    nameen = models.CharField(max_length=255)

    descar = models.TextField()
    descen = models.TextField()

    # guestgroup = models.ForeignKey(Groups,on_delete=models.CASCADE)
    # mealplan=models.ForeignKey(MealPlan,on_delete=models.CASCADE)

    roomguests=models.TextField(null=True,blank=True)
    roombeds=models.TextField(null=True,blank=True)
    roomicons=models.TextField(null=True,blank=True)


    main=models.ImageField(upload_to='rooms/logos')
    first_image=models.ImageField(upload_to='rooms/images',blank=True,null=True)
    second_image=models.ImageField(upload_to='rooms/images',blank=True,null=True)
    third_image=models.ImageField(upload_to='rooms/images',blank=True,null=True)


    
    
    def __str__(self) -> str:
        return f'{self.namear} {self.nameen}'
class RoomPhotos(models.Model):

    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name='photos')
    photo=models.ImageField(upload_to='room/images',blank=True,null=True)  
class ManualReservationCustomer(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    nationality=models.CharField(max_length=255)

class RoomBedOptions(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name='bedoptions')

    number=models.PositiveSmallIntegerField()
  
class BedOptionDetails(models.Model):
    name=models.CharField(max_length=255)
    
    number=models.SmallIntegerField()
    room=models.ForeignKey(RoomBedOptions,on_delete=models.CASCADE,related_name='bed_details')



class RoomGuestoption(models.Model):
    
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name='guestoptions')
    number=models.PositiveSmallIntegerField()    
class GuestOptionDetails(models.Model):
    name=models.CharField(max_length=255)
    
    number=models.SmallIntegerField()
    room=models.ForeignKey(RoomGuestoption,on_delete=models.CASCADE,related_name='guests_details')    
class Manualreservations(models.Model):
    MANUL_ChOICES=[
        ('req','requested'),('w','waiting'),
        ('cnc','collection not confirmed'),('con','confirmed'),
        ('col','collected'),('com','completed'),('can','canceled')
    ]
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    bedoption=models.ForeignKey(RoomBedOptions,on_delete=models.CASCADE)
    guestoption=models.ForeignKey(RoomGuestoption,on_delete=models.CASCADE)
    status=models.CharField(max_length=255,choices=MANUL_ChOICES)


    # roomoption=models.CharField(max_length=255)
    #periods\
class Icon(models.Model):
    iconschoices=[
        ('h','hotel'),
              ('g','guets'),  ('b','bed') , ('m','meal') , ('r','room')
    ]
    name=models.CharField(max_length=255)
    news_img = models.FileField(upload_to="icons", validators=[FileExtensionValidator(['png', 'jpeg', 'svg'])])

    type=models.CharField(max_length=255,choices=iconschoices)   
class Periods(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)

    startdate=models.DateField()
    enddate=models.DateField() 

class StopSale(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)

    startdate=models.DateField()
    enddate=models.DateField() 

class Rate (models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    mealplan=models.ForeignKey(MealPlan,on_delete=models.CASCADE)
    period=models.ForeignKey(Periods,on_delete=models.CASCADE)
    group=models.ForeignKey(Groups,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE) 
    netrate=models.FloatField(null=True,blank=True)               

class Update (models.Model):

    choices=[
     ('f','fixed') , ('r','related') , ('p','percent')
    ]
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    mealplan=models.ForeignKey(MealPlan,on_delete=models.CASCADE)
    period=models.ForeignKey(Periods,on_delete=models.CASCADE)
    group=models.ForeignKey(Groups,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE) 
    type=models.CharField(max_length=255,choices=choices) 
    u_tupe=models.CharField(max_length=255,choices=[('u','update'),('d','downgrade')])  
    percent=models.SmallIntegerField(null=True)
    value=models.SmallIntegerField(null=True)
    def __str__(self):
        return f'{self.id}'

class UpdateDetails(models.Model):
    update=models.ForeignKey(Update,on_delete=models.CASCADE)
    period=models.ForeignKey(Periods,on_delete=models.CASCADE)
    val=models.SmallIntegerField(null=True)
class Availability(models.Model):
    type=models.CharField(max_length=255,choices=[('all','all periods'),('c','custom periods')])    
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    val=models.PositiveIntegerField(null=True)
class AvailabilityperoiodsDetails(models.Model):
    period=models.ForeignKey(Periods,on_delete=models.CASCADE)
    availability=models.ForeignKey(Availability,on_delete=models.CASCADE)


    

class Supplement(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    amount=models.PositiveIntegerField()
    group=models.ForeignKey(Groups,on_delete=models.CASCADE)      


class Users(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)

    username=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.EmailField()
    bitrthdate=models.DateField()

class Emails(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    email=models.EmailField()
class ExtraServices(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    desc=models.TextField()
    group=models.ForeignKey(Groups,on_delete=models.CASCADE)
    price=models.SmallIntegerField()

class Notification(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.TextField()
    
    
    

        