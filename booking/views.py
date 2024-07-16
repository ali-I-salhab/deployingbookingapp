from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from .models import Availability, AvailabilityperoiodsDetails, BedOptionDetails, GroupCountries, GuestOptionDetails, Hotel,Icon,Groups,MealPlan, Periods,Photos, Rate,Room,Manualreservations, RoomBedOptions, RoomGuestoption, StopSale, Supplement, Update, UpdateDetails, Users
from .serilaizers import AddRoomSerializer, AvailabilitySerializer, AvailabilitydetailsSerializer, BedOptionDetailsSerializer,BedoptionSerializer, GroupCountriesSerializer, GuestOptionDetailsSerializer, GuetsoptionsSerializer,IconsSerializer, HotelSerializer,ManualReservationSerilaizer,GroupSerializer, PeriodsSerializer, RateSerializer,RoomSerializer,PhotosSerializer,MealplanlSerializer, RoombedoptionSerializer, StopSaleSerializer, SupplementSerializer, UpdateDetailsSerializer,UpdateHotelserializer,ListHotelsSerializer, UpdateSerializer, UsersSerializer
# Create your views here.
from rest_framework.parsers import MultiPartParser,FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
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
        return super().get_serializer_context()


    def get_serializer_class(self):
            if self.action in('list','create'):
                return ListHotelsSerializer
             
       
            return HotelSerializer
    
    def get_queryset(self):
        # if(self.request.method=='GET'):
        #     print(self.kwargs['id'])

        # if(self.request.method=='PUT'):
            
        #     Hotel.objects.get(id=self.kwargs['pk']).logo.delete(save=True)
        if(self.request.method=='DELETE'):
            print('delete method ---------->')
            # hotel/logos/Frame_48096168_vpZytal.png
            print(  Hotel.objects.get(id=self.kwargs['pk']).logo)
            Hotel.objects.get(id=self.kwargs['pk']).logo.delete(save=True)
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
    serializer_class=MealplanlSerializer
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

    serializer_class=StopSaleSerializer    

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
