from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.

# hotels
# name	phone	review	stars	category	location	website	email	PlusCode	close time	lat	long	Instagram	facebook	Linked-in	twitter	photos

class Hotel(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    namear = models.CharField(max_length=255,null=True,blank=True)
    nameen = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)

    review = models.CharField(max_length=255,null=True,blank=True)

    website = models.CharField(max_length=255,null=True,blank=True,default="")

    email = models.CharField(max_length=255,null=True,blank=True,default="")
    password = models.CharField(max_length=255,null=True,blank=True,default="")


    PlusCode = models.CharField(max_length=255,null=True,blank=True,default="")
    close_time = models.CharField(max_length=255,null=True,blank=True,default="")
    Instagram = models.CharField(max_length=255,null=True,blank=True,default="")
    facebook = models.CharField(max_length=255,null=True,blank=True,default="")
    Linked_in = models.CharField(max_length=255,null=True,blank=True,default="")
    twitter = models.CharField(max_length=255,null=True,blank=True)
    sales_email = models.EmailField(null=True,blank=True,default="")

    sales_phone = models.CharField(max_length=255,null=True,blank=True,default="")
    availabilityandrateprovider = models.CharField(max_length=255,null=True,blank=True,choices=[('ta','traveky admin'),('aa','account admin')],default='ta')
    b2b=models.SmallIntegerField(null=True,default=15)
    b2c=models.SmallIntegerField(null=True,default=15)


    reservation_email = models.EmailField(null=True,blank=True,default="")

    reservation_phone = models.CharField(max_length=255,null=True,blank=True,default="")

    accounting_email = models.EmailField(null=True,blank=True,default="")

    accounting_phone = models.CharField(max_length=255,null=True,blank=True,default="")
    payment=models.CharField(max_length=255,null=True,blank=True,choices=[('hpg','Hotel Payment Geteway'),('tppg','Travky Partner Payment Geteway'),('tgpg','Travky Gartner Payment Geteway')])



    logo=models.ImageField(upload_to='hotel/logos',blank=True,null=True)
    Category = models.CharField(max_length=255,null=True,blank=True)
    HoteStars = models.SmallIntegerField(null=True,blank=True,default=0)
    country = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    postcode = models.CharField(max_length=255,null=True,blank=True,default="")
    lat = models.FloatField(null=True,blank=True,default=0)
    long=models.FloatField(null=True,blank=True,default=0)
    descar=models.TextField(null=True,blank=True,default="")
    descen=models.TextField(null=True,blank=True,default="")
    policyen=models.TextField(null=True,blank=True,default="")
    policyar=models.TextField(null=True,blank=True,default="")
    icons=models.CharField(max_length=25,null=True,blank=True,default="")
    user_name=models.CharField(max_length=255,blank=True,null=True,default="")
    email=models.EmailField(blank=True,null=True,default="")
    
    def save(self, *args, **kwargs):

        print('save---------------------->')
        
        print(args)
        print(kwargs)
        
        super(Hotel, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.id}'
    class Meta:
        ordering=['-id']
# Groups
# null in field makeit nullable in database level
# blank in field make it nullable in admin site
class ContractAttachement(models.Model):
    hotel=models.ForeignKey(Hotel,related_name='contractAttachment',on_delete=models.CASCADE)
    file=models.FileField(upload_to="contract_attachement", validators=[FileExtensionValidator(['pdf'])])
class Groups(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="groups")
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
    
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='mealplans')

    nameen=models.CharField(max_length=255)
    namear=models.CharField(max_length=255)
    descar=models.TextField()
    descen=models.TextField()
    status=models.BooleanField()
    price=models.IntegerField(null=True)
    type=models.CharField(max_length=255,choices=[('inr','included net-rate'),('as','as supplement')])
# photos




class Photos(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='photos')
    phototype=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='hotel/photos')

# rooms
class Room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='rooms')

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
        return f'{self.id}'
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
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='Manualreservations')
    
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
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='periods')

    startdate=models.DateField()
    enddate=models.DateField() 

class StopSale(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='stopsale')

    startdate=models.DateField()
    enddate=models.DateField() 

class Rate (models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="rates")
    mealplan=models.ForeignKey(MealPlan,on_delete=models.CASCADE)
    period=models.ForeignKey(Periods,on_delete=models.CASCADE)
    group=models.ForeignKey(Groups,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE) 
    netrate=models.FloatField(null=True,blank=True)               

class Update (models.Model):

    choices=[
     ('f','fixed') , ('r','related') , ('p','percent')
    ]
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='update')
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
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='Supplement')
    name=models.CharField(max_length=255)
    amount=models.PositiveIntegerField()
    group=models.ForeignKey(Groups,on_delete=models.CASCADE)      


class Users(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='users')

    username=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.EmailField()
    bitrthdate=models.DateField()

class Emails(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='emails')
    email=models.EmailField()
class ExtraServices(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='extra_services')
    name=models.CharField(max_length=255)
    desc=models.TextField()
    group=models.ForeignKey(Groups,on_delete=models.CASCADE)
    price=models.SmallIntegerField()

class Notification(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='Notification')
    title=models.CharField(max_length=255)
    content=models.TextField()
    
    
    

        