from io import BytesIO
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from .models import Availability, AvailabilityperoiodsDetails, BedOptionDetails, ContractAttachement, Emails, GroupCountries, GuestOptionDetails, Hotel,Icon,Groups,MealPlan, Notification, Periods,Photos, Rate,Room,Manualreservations, RoomBedOptions, RoomGuestoption, StopSale, Supplement, Update, UpdateDetails, Users
from .serilaizers import AddRoomSerializer, AddStopSaleSerializer, AdminListHotelsSerializer, AvailabilitySerializer, AvailabilitydetailsSerializer, BedOptionDetailsSerializer,BedoptionSerializer, ContractAttachementSerilizer, EmailsSerilizer, GroupCountriesSerializer, GuestOptionDetailsSerializer, GuetsoptionsSerializer,IconsSerializer, HotelSerializer,ManualReservationSerilaizer,GroupSerializer, MealplanSerializer, NotificationSerilizer, PeriodsSerializer, RateSerializer,RoomSerializer,PhotosSerializer, RoombedoptionSerializer, SuperAdminListHotelsSerializer, SuperAdminPhotosSerializer, SupplementSerializer, UpdateDetailsSerializer,UpdateHotelserializer, UpdateSerializer, UsersSerializer, ViewstopSaleSerializer
# Create your views here.
from rest_framework.parsers import MultiPartParser,FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from .functions import delete_hotel_files
import numpy as np
from core.models import User
from django.core.mail import send_mail
import os
import requests
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice

# topic = "A topic"
# FCMDevice.objects.handle_subscription(True, topic)
# FCMDevice.send_topic_message(Message(data={...}), "TOPIC NAME")

def delete_old_file(path_file):
    print('trigger delete method')
    #Delete old file when upload new one
    if os.path.exists(path_file):
        print("100 delete complete")
        os.remove(path_file)
def handlevalue(paraname):
    if  pd.isna(paraname):
        return ""
     
    else :
        return paraname
def handleintvalue(paraname):
    if  pd.isna(paraname):
        return 0
     
    else :
        return paraname
    
    
# =============================upload excel file

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    permission_classes = [permissions.IsAuthenticated]
									 	

    def put(self, request, format=None):
        print(request.data)
        # send_mail("from booking app","hellow word","settings.EMAIL_HOST_USER",["alysalhab5@gmail.com"])
        try:
            file_obj = request.data['file']
            file_content = file_obj.read()
            df = pd.read_excel(BytesIO(file_content), engine='openpyxl')
            df=pd.DataFrame(df)
            print('current usrt is ')
            print(user)
          
            user=User.objects.get(id=self.request.user.id)
      
            df1 = df.replace(np.nan, None)

 
             
            
            hotels=[
                Hotel(user=user
                      ,nameen=j['name'],
                      namear="Not selected " if not 'namear' in df else   j['namear'],
                      phone=handlevalue(j['phone'])
                      ,HoteStars=handleintvalue(j['stars']),
                      review=handlevalue(j['review']),
                      website=handlevalue(j['website']),
                      email=handlevalue(j['email']),
                      PlusCode=handlevalue(j['PlusCode']),
                      close_time=handlevalue(j['close time']),
                      Category=handlevalue(j['category']),
                    country= "Not selected " if not 'country' in df else   j['country'],
                      city="Not selected " if not 'city' in df else   j['city'],
                      location=handlevalue(j['location']),
                    #   postcode=j['stars'],
                      lat=handleintvalue(j['lat']),
                      long=handleintvalue(j['long']),
                      descar="Not descripted " if not 'descar' in df else   j['descar'],
                       descen="Not descripted " if not 'descen' in df else   j['descen'],
                        policyen="Not selected " if not 'policyen' in df else   j['policyen'],
                         policyar="Not selected " if not 'policyar' in df else   j['policyar'],
                          icons="Not selected " if not 'icons' in df else   j['icons'],
                          Instagram=handlevalue(j['Instagram']),
                          facebook=handlevalue(j['facebook']),
                          Linked_in=handlevalue(j['Linkedin']),
                          twitter=handlevalue(j['twitter']),

                      
                      
                      
                      
                      ) for i,j in  df1.iterrows()
            ]
            Hotel.objects.bulk_create(hotels)
      

        
            return Response({'status': 'success', 'message': 'File uploaded.'})
        except Exception as e:
            error_message = str(e)
            if error_message=="File is not a zip file" :
                error_message="File is not a Excel file"

            return Response({'status': 'error', 'message': error_message})



class Hotelviewset(ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    http_method_names=['post','get','delete','patch']

   
    
    # print(self.re)
    # # queryset=Hotel.objects.all()
    # def get_serializer_context(self):
    #     return super().get_serializer_context()
    def get_serializer_context(self):
 
        # print('Hello From Serializer context Meyhod >>>>?')
        print(self.action)
        if (self.action =='partial_update'):
            print('in conditoin')
        #     print('here method is retrive')
            return {'id' : self.kwargs['pk']}
        
        return {'userid':self.request.user.id}


    def get_serializer_class(self):
            if self.action in('list','create'):
                if 'type' in  self.request.headers and self.request.headers['type']=='superadmin':
                           print('return SuperAdminListHotelsSerializer')
                
                           return SuperAdminListHotelsSerializer
                else :
                            print('header with out type')
                            return AdminListHotelsSerializer
             
       
            return SuperAdminListHotelsSerializer
    
    def get_queryset(self):
        device = FCMDevice.objects.first()
        device.send_message( Message(notification=Notification(title="title", body="body", image="image_url")))
        # send_fcm_message("ecTeTKL_RKuD9JSKuXVCCp:APA91bG1Aev00a8SvXRYY3UiUmeV6a-H87qGdyEWZ175K9cqsfLg8GABZ185zoHoT2U6PTaIIIlxt3w5oAqJa8e03srQkfQqgYONXa0OtzR6xTafXTyj6rHXmb4o6m2W5EHdemoO24g0","django from token","this is me")

      
        # if(self.request.method=='GET'):
        #     print(self.kwargs['id'])

        # if(self.request.method=='PUT'):
            
        #     Hotel.objects.get(id=self.kwargs['pk']).logo.delete(save=True)
        if(self.request.method=='DELETE'):
            print('delete method ---------->')
            # hotel/logos/Frame_48096168_vpZytal.png
            print(  Hotel.objects.get(id=self.kwargs['pk']).logo)
            delete_hotel_files(self.kwargs['pk'])
 
        print(self.request.user)
        return Hotel.objects.filter(user=self.request.user.id)
    serializer_class=HotelSerializer
class Groupviewset(ModelViewSet):
    def create(self, request, *args, **kwargs):
        print("create ")
        group= super().create(request, *args, **kwargs)
        hotel=Hotel.objects.get(id=group.data['hotel'])
        rates=Rate.objects.all().filter(hotel=group.data['hotel'])
        for r in Room.objects.all():    
            for m in MealPlan.objects.all():
                for p in Periods.objects.all():
                    for g in Groups.objects.all():
                            if(Rate.objects.filter(hotel=hotel,room=r,mealplan=m,group=g,period=p).exists()):
                                continue
                            else:
                                Rate.objects.create(hotel=hotel,room=r,mealplan=m,group=g,period=p,netrate=None)
        return group                            
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['hotel']
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        
        print('groups list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        
        return Groups.objects.filter(hotel__in=my_values)

    serializer_class=GroupSerializer
    
class Roomviewset(ModelViewSet):
    def get_serializer_context(self):
        print('Room serilaizer context')
        print(self.action)
        return {}
    def create(self, request, *args, **kwargs):
        print("CReate new RRoom")
        # print(MealPlan.objects.all().count())
        # print(Periods.objects.all().count())
        # print(Groups.objects.all().count())
        mcount=MealPlan.objects.all().count()
        pcount=Periods.objects.all().count()
        gcount=Groups.objects.all().count()


        a =super().create(request, *args, **kwargs)
        print(a.data)
        
        hotel=Hotel.objects.get(id=a.data['hotel'])
        room=Room.objects.get(id=a.data['id'])
        
        if(mcount and pcount and gcount):
            for m in MealPlan.objects.all():
                for p in Periods.objects.all():
                    for g in Groups.objects.all():
                        print("-------------->")
                        print(m,p,g)
                        Rate.objects.create(hotel=hotel,room=room,mealplan=m,group=g,period=p,netrate=None)
        print(a.data['id'])
        return Response(a.data)
        # return super().create(request, *args, **kwargs)
    def create_rate():
        print("Create rate")
    def get_queryset(self):
        print(self.action)
        print(self.request.method)
        print("get query set ")
        if self.action=='GET':
            print("GEt data")
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        return Room.objects.filter(hotel__in=my_values)
   
    def get_serializer_class(self):
        print('Room serializer class is ')
        print(self.action)
        if self.request.method=='post':
            return AddRoomSerializer
             
        return RoomSerializer     
class Mealplanviewset(ModelViewSet):
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['hotel']
    def create(self, request, *args, **kwargs):
        mealplane= super().create(request, *args, **kwargs)
        hotel=Hotel.objects.get(id=mealplane.data['hotel'])
        rates=Rate.objects.all().filter(hotel=mealplane.data['hotel'])
       
        for r in Room.objects.all():    
            for m in MealPlan.objects.all():
                for p in Periods.objects.all():
                    for g in Groups.objects.all():
                            if(Rate.objects.filter(hotel=hotel,room=r,mealplan=m,group=g,period=p).exists()):
                                continue
                            else:
                                Rate.objects.create(hotel=hotel,room=r,mealplan=m,group=g,period=p,netrate=None)
                    
                        
        return Response(mealplane.data)

    def get_queryset(self):
        
        print('meal plans list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return MealPlan.objects.filter(hotel__in=my_values)
    def get_serializer_class(self):
        print('serilizer class  plans list query set--------------->')

        # print(self.data)

        return MealplanSerializer
class Photosviewset(ModelViewSet):
    
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['hotel']
    def get_queryset(self):
        print('phot list list query set--------------->')
        
        
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return Photos.objects.filter(hotel__in=my_values)
    
    
    serializer_class=PhotosSerializer    
class RoomGuetsoptionsviewset(ModelViewSet):
    def get_serializer_context(self):
        print("======================Room Guest options")
        print(self.kwargs)
        return {'roomid':self.kwargs['room_pk']}
    queryset=RoomGuestoption.objects.all()
    serializer_class=GuetsoptionsSerializer

class RoomGuestoptionsDetailsviewset(ModelViewSet):
    def get_serializer_context(self):
        print("======================Room Guest options")
        print(self.kwargs)
        return {'optionid':self.kwargs['details_pk']}
    queryset=GuestOptionDetails.objects.all()
    serializer_class= GuestOptionDetailsSerializer       
class RoomBedoptionsDetailsviewset(ModelViewSet):
    def get_serializer_context(self):
        print("======================Room Guest options")
        print(self.kwargs)
        return {'optionid':self.kwargs['details_pk']}
    queryset=BedOptionDetails.objects.all()
    serializer_class= BedOptionDetailsSerializer   

class RoomBedoptionsviewset(ModelViewSet):
    def get_serializer_context(self):
        print("======================Room Guest options")
        print(self.kwargs)
        return {'roomid':self.kwargs['room_pk']}
    def get_queryset(self):
        return RoomBedOptions.objects.filter(room=self.kwargs['room_pk'])

    def get_serializer_class(self):
        print("ddd")
        print(self.action)
        if(self.action =='retrieve'):
           return BedoptionSerializer
        else :
            return RoombedoptionSerializer


class IconsViewset(ModelViewSet):

    filter_backends=[DjangoFilterBackend]
    filterset_fields=['type']
    def get_queryset(self):
        if(self.request.method=='DELETE'):
            Icon.objects.get(id=self.kwargs['pk']).news_img.delete(save=True)
        print(self.request.user)
        return Icon.objects.all()
 
    serializer_class=    IconsSerializer    
class ManualReservation(CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,GenericViewSet):
    queryset=Manualreservations.objects.all()
    serializer_class=ManualReservationSerilaizer    

class GroupCountriesViewset(ModelViewSet):
    def get_queryset(self):
        
        print('groups list query set--------------->')
        print(self.kwargs)
        group=Groups.objects.get(id=self.kwargs['groups_pk'])
        # print(self.request.query_params['hotel'])
        # print(self.request.user)

        countries=GroupCountries.objects.filter(group=group)
       
        
        return countries
    
                
                        
        return Response(group.data)
    def get_serializer_context(self):
        print(self.kwargs)
        
        return {'group_id':self.kwargs['groups_pk']}
   
    serializer_class= GroupCountriesSerializer       
class Stopsaleviewset(ModelViewSet):
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['hotel']

    def get_queryset(self):
        
        print('groups list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return StopSale.objects.filter(hotel__in=my_values)

    def get_serializer_class(self):
        print(self.request.method)
        if(self.request.method=='POST'):
            return AddStopSaleSerializer
        return ViewstopSaleSerializer

class Periodsviewset(ModelViewSet):
    def create(self, request, *args, **kwargs):
        period= super().create(request, *args, **kwargs)
        hotel=Hotel.objects.get(id=period.data['hotel'])
        rates=Rate.objects.all().filter(hotel=period.data['hotel'])
        
        for r in Room.objects.all():    
            for m in MealPlan.objects.all():
                for p in Periods.objects.all():
                    for g in Groups.objects.all():
                            if(Rate.objects.filter(hotel=hotel,room=r,mealplan=m,group=g,period=p).exists()):
                                continue
                            else:
                                Rate.objects.create(hotel=hotel,room=r,mealplan=m,group=g,period=p,netrate=None)
                
                        
        return Response(period.data)
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['hotel']

    def get_queryset(self):
        # print("-----------> Rate")
        # mealplan=MealPlan.objects.get(id=3)
        # period= Periods.objects.get(id=1)
        # group=Groups.objects.get(id=4)
        # hotel=Hotel.objects.get(id=40)
        # room=Room.objects.first()

        
        print('groups list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return Periods.objects.filter(hotel__in=my_values)

    serializer_class=PeriodsSerializer        


class Rateviewset(ModelViewSet):
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['hotel']

    def get_queryset(self):
        
        print('groups list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return Rate.objects.filter(hotel__in=my_values)

    serializer_class=RateSerializer 


class Updatesviewset(ModelViewSet):
  

    filter_backends=[DjangoFilterBackend]
    filterset_fields=['hotel']

    def get_queryset(self):
        
        print('groups list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return Update.objects.filter(hotel__in=my_values)

    serializer_class=UpdateSerializer                     

class UpdateDetailsviewset(ModelViewSet):
    def get_serializer_context(self):
        print("======================update serilaizer")
        print(self.kwargs)
        return {'update_id':self.kwargs['updates_pk']}
    queryset=UpdateDetails.objects.all()
    serializer_class= UpdateDetailsSerializer  
class Availabilityviewset(ModelViewSet):
    def perform_create(self, serializer):
        print("=========================+++++++++++++++++++++++")
        print('after create new availabiltuy object')
        print(self.request.data['type'])
        new_availability=serializer.save()
        print(new_availability.id)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        periods=Periods.objects.filter(hotel__in=my_values)
        for p in periods:
            if self.request.data['type']=='all':
                 AvailabilityperoiodsDetails.objects.create(availability=new_availability,period=p,val=self.request.data['val'])
            else:
                 AvailabilityperoiodsDetails.objects.create(availability=new_availability,period=p)
        return super().perform_create(serializer)
    def get_serializer_context(self):
       user=self.request.user.id


        
       return {'userid':user}

    queryset=Availability.objects.all()
    serializer_class= AvailabilitySerializer  

class Availabilitydetailsviewset(ModelViewSet):

    def get_queryset(self):
        print("Availabilitydetailsviewset------------->")
        print(self.kwargs)
        return AvailabilityperoiodsDetails.objects.filter(availability=self.kwargs['availability_pk'])
    serializer_class= AvailabilitydetailsSerializer      
class Usersviewset(ModelViewSet):
    # def get_serializer_context(self):
    #     print("======================update serilaizer")
    #     print(self.kwargs)
    #     return {'update_id':self.kwargs['updates_pk']}
    queryset=Users.objects.all()
    serializer_class= UsersSerializer  
class Supplementviewset(ModelViewSet):
    # def get_serializer_context(self):
    #     print("======================update serilaizer")
    #     print(self.kwargs)
    #     return {'update_id':self.kwargs['updates_pk']}
    queryset=Supplement.objects.all()
    serializer_class= SupplementSerializer  
class Contractviewset(ModelViewSet):

    def get_serializer_context(self):
        print("======================update serilaizer")
        print(self.kwargs)
        return {'hotel_id':self.kwargs['hotels_pk']}
        
    def get_queryset(self):
        print(self.kwargs)
        print(self.request.method)
        if self.request.method=='DELETE':
            ContractAttachement.objects.get(id=self.kwargs['pk']).file.delete(save=True)

          
        
        return ContractAttachement.objects.filter(hotel=self.kwargs['hotels_pk'])
    serializer_class= ContractAttachementSerilizer  
class SuperadminPhotosviewset(ModelViewSet):
    def get_serializer_context(self):
        return {'hotelid':self.kwargs['hotels_pk']}
    
   
    def get_queryset(self):
        print("---------------------")
        print(self.kwargs)
        if self.request.method=='DELETE':
            Photos.objects.get(id=self.kwargs['pk']).photo.delete(save=True)

            print('Delete     photp')
 
        return Photos.objects.filter(hotel_id=self.kwargs['hotels_pk'])
    
    
    serializer_class=SuperAdminPhotosSerializer       
class Notificationsviewset(ModelViewSet):
    # def get_serializer_context(self):
    #     print("======================update serilaizer")
    #     print(self.kwargs)
    #     return {'update_id':self.kwargs['updates_pk']}
    serializer_class= NotificationSerilizer      

    def get_queryset(self):
        
        print('groups list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return Notification.objects.filter(hotel__in=my_values)    
class Emailsviewset(ModelViewSet):
    # def get_serializer_context(self):
    #     print("======================update serilaizer")
    #     print(self.kwargs)
    #     return {'update_id':self.kwargs['updates_pk']}
    serializer_class= EmailsSerilizer      

    def get_queryset(self):
        
        print('groups list query set--------------->')
        # print(self.request.query_params['hotel'])
        # print(self.request.user)
        userhotel=Hotel.objects.filter(user=self.request.user.id)
        my_values = [item.id for item in userhotel]
        print(my_values)
        return Emails.objects.filter(hotel__in=my_values)        