from rest_framework import serializers
import re
from .models import Availability, AvailabilityperoiodsDetails, BedOptionDetails, ContractAttachement, Emails, ExtraServices, GroupCountries, GuestOptionDetails, Hotel, Icon, Notification, Periods, Rate,Room,Photos,MealPlan,Groups,Manualreservations,RoomBedOptions,RoomGuestoption, StopSale, Supplement, Update, UpdateDetails, Users


import os

def delete_old_file(path_file):
    #Delete old file when upload new one
    if os.path.exists(path_file):
        os.remove(path_file)
class PhotosSerializer(serializers.ModelSerializer):
        class Meta:
            model=Photos
            fields='__all__'  
class SuperAdminPhotosSerializer(serializers.ModelSerializer):
        hotel=serializers.CharField(read_only=True)
        def create(self, validated_data):
              print('create new photo')
              return Photos.objects.create(hotel_id=self.context['hotelid'],**validated_data)
        class Meta:
            model=Photos
            fields=['phototype','photo','id','hotel']  
class ContractAttachementSerilizer(serializers.ModelSerializer):
 
      def create(self, validated_data):
            hotelid=self.context['hotel_id']
            return ContractAttachement.objects.create(hotel_id=hotelid,**validated_data)

            
      class Meta:
            model=ContractAttachement
            fields=['id','file']

class HotelSerializer(serializers.ModelSerializer):
      
      #   user=serializers.CharField(read_only=True)
      #   logo=serializers.FilePathField('media/hotel/logos', match=None, recursive=False, allow_files=True, allow_folders=False, required=None,)
      # logo=serializers.SerializerMethodField('get_avatar_url')
      # def get_avatar_url(self, obj):
      # #   request = self.context.get('id')
      # #   if obj.logo.url!=None:
              
      # #      return (obj.logo.url)
      # #   else :return None
      def save(self, **kwargs):
            print('save method called')

          
            # print(self.context['id'])
            oldlogo=Hotel.objects.get(id=self.context['id'])
            print('-------------------old logo--------------=')
            if (oldlogo.logo):
                print("logggggggggggggo")
                print(oldlogo.logo.url)
                if(self.validated_data.get('logo')==None):
                        print(self.validated_data)
                        self.validated_data['logo']=oldlogo.logo.url[7:]
                        print('none')    
            print('-------------------new logo--------------=')
            print(self.validated_data.get('logo'))
            return super().save(**kwargs)
      # def update(self, instance : Hotel, validated_data):
      #       print('-----update-------')
      #       print('previous data is ')
      #       print(self.data)
            
      #       print('coming from post action data is ')
      #       print(validated_data)
      #       print(validated_data.get('logo'))
      #       if(validated_data.get('logo')==None):
      #             validated_data=instance.logo.url
                  
      #             print('logo null')
      #       instance.lat="122" 
      #       print("------------log0")
      #       print(instance.logo)
      #       # instance.logo='eeeeeeeee'
      #       instance.save()
      #       print(instance.logo)
      #       return instance
      # logo=serializers.ImageField(required=False)
      def get_hotel_image(self,  h:Hotel):
            
           
            print(self.context)
            return h.logo.url
      

      class Meta:
            model=Hotel
            fields=['id','logo','namear','nameen','user','Category','HoteStars','country','city','location','postcode','lat','long','descen','descar','policyen','icons','user']    
class UpdateHotelserializer(serializers.ModelSerializer):
      class Meta:
            model=Hotel
            fields='__all__'
class RoombedoptionSerializer(serializers.ModelSerializer):
      # details=serializers.SerializerMethodField(method_name='get_setails')
      # def get_setails(self, obj):
      #       print('details Customizing ------------------>>>>>')
      #       print(self.context.get('view').kwargs.get('pk'))
            
            
      #       queryset= BedOptionDetails.objects.filter(room__room=self.context.get('view').kwargs['pk'])
      #       return BedOptionDetailsSerializer(queryset, many=True).data
#  here the error ----------->
      # userchoices=Icon.objects.filter(type='b')
      # my_choices = [item.name for item in userchoices]
      print("------------------->")
      # print(my_choices)
      def create(self, validated_data):
            print('from create bed option seralizer')
            print(self.context['roomid'])
      
            room=Room.objects.get(id=self.context['roomid'])
            return RoomBedOptions.objects.create(room=room,**validated_data)
      # type=serializers.ChoiceField(choices=my_choices)
      class Meta :
            model=BedOptionDetails
            fields=['number','id',]                 
class BedoptionSerializer(serializers.ModelSerializer):
      details=serializers.SerializerMethodField(method_name='get_setails')
      def get_setails(self, obj):
            print('details Customizing ------------------>>>>>')
            print(obj.room.id)
            
            queryset=None
           
            queryset= BedOptionDetails.objects.filter(room__room=obj.room.id)
            return BedOptionDetailsSerializer(queryset, many=True).data

      # userchoices=Icon.objects.filter(type='b')
      # my_choices = [item.name for item in userchoices]
      # print("------------------->")
      # print(my_choices)
      def create(self, validated_data):
            print('from create bed option seralizer')
            print(self.context['roomid'])
      
            room=Room.objects.get(id=self.context['roomid'])
            return RoomBedOptions.objects.create(room=room,**validated_data)
      # type=serializers.ChoiceField(choices=my_choices)
      class Meta :
            model=BedOptionDetails
            fields=['number','id','details']     
class BedOptionDetailsSerializer(serializers.ModelSerializer):
      details=BedoptionSerializer(many=True,read_only=True)
      

      # userchoices=Icon.objects.filter(type='b')
      # my_choices = [item.name for item in userchoices]
      name=serializers.CharField(max_length=255)


      def create(self, validated_data):
            print('--------------------------------option id')
            print(self.context['optionid'])
      
            room=RoomBedOptions.objects.get(id=self.context['optionid'])
            return BedOptionDetails.objects.create(room=room,**validated_data)

        
      class Meta:
            model=BedOptionDetails
            fields=['id','name','number','details']

class GuestOptionDetailsSerializer(serializers.ModelSerializer):
      # userchoices=Icon.objects.filter(type='g')
      # my_choices = [item.name for item in userchoices]
      name=serializers.CharField(max_length=255)


      def create(self, validated_data):
            print('--------------------------------option id')
            print(self.context['optionid'])
      
            guest=RoomGuestoption.objects.get(id=self.context['optionid'])
            return GuestOptionDetails.objects.create(room=guest,**validated_data)

        
      class Meta:
            model=BedOptionDetails
            fields=['id','name','number']

class GuetsoptionsSerializer(serializers.ModelSerializer):
      details=GuestOptionDetailsSerializer(many=True,read_only=True)

      # userchoices=Icon.objects.filter(type='g')
      # my_choices = [item.name for item in userchoices]
      # print("------------------->")
      # print(my_choices)
      def create(self, validated_data):
            print('from create bed option seralizer')
            print(self.context['roomid'])
      
            room=Room.objects.get(id=self.context['roomid'])
            return RoomGuestoption.objects.create(room=room,**validated_data)
      # type=serializers.ChoiceField(choices=my_choices)
      class Meta :
            model=RoomBedOptions
            fields=['id','number','details']    
          


class RoomSerializer(serializers.ModelSerializer):
        bedoptions=BedoptionSerializer(many=True,read_only=True)
        guestoptions=GuetsoptionsSerializer(many=True,read_only=True)
        
        class Meta:
            model=Room
            fields=['id','hotel','nameen','namear','descar','descen','roomguests','roombeds','roomicons','main','first_image','second_image','third_image','bedoptions','guestoptions']


class AddRoomSerializer(serializers.ModelSerializer):
        bedoptions=serializers.CharField(max_length=255)
        guestoptions=serializers.CharField(max_length=255)
        
        class Meta:
            model=Room
            fields=['id','nameen','namear','descar','descen','roomguests','roombeds','roomicons','main','first_image','second_image','third_image','bedoptions','guestoptions']


















        
class MealplanSerializer(serializers.ModelSerializer):
      # def __init__(self, *args, **kwargs):
      #   super(MealplanSerializer, self).__init__(*args, **kwargs)
      #   print(self.initial_data)

      #   if 'type' in self.initial_data and self.initial_data['type'] == 'as':
      #       self.fields['dynamic_field'] = serializers.CharField()
      #   else:
      #       self.fields.pop('dynamic_field', None)
      # def get_fields(self):
      #   fields = super(MealplanSerializer,self).get_fields()
      #   print(self.instance.get('type'))

      #   # Add field4 only if field1 is equal to 'value'
      # #   if self.instance.type == 'as':
      # #       fields['p'] = serializers.CharField(max_length=255)

      #   return fields
      # # def to_representation(self, instance):
      # #   data = super(MealplanSerializer, self).to_representation(instance)
        
      # #   # Include field4 only if field1 is equal to 'value'
      # #   if data['type'] == 'as':
      # #       data['value'] = data['price']
        
      # #   return data

            
      class Meta:
            model=MealPlan
            fields=['id','hotel','price','nameen','namear','descar','descen','type','status']              
                                                    
class GroupCountriesSerializer(serializers.ModelSerializer):
      group=serializers.CharField(read_only=True,max_length=255)
      
      def create(self, validated_data):
            # self.context['group_id']
            print(validated_data)
            list=re.split(r',',validated_data['name'])
            group=Groups.objects.get(id=self.context['group_id'])
            print(list)
            countries = [GroupCountries(name=l,group=group) for l in list[1:]]
            GroupCountries.objects.bulk_create(countries)
            print(countries)
            return GroupCountries.objects.create(group=group,name=list[0])
      class Meta:
            model=GroupCountries
            fields=['id','name','group']           
class GroupSerializer(serializers.ModelSerializer):
        countries=GroupCountriesSerializer(many=True,required=False,read_only=True)
        
        class Meta:
            model=Groups
            fields=['id','hotel','countries','currency','name','status']                

class SimpleHotelSerializer(serializers.ModelSerializer):
      class Meta :
            model=Hotel
            fields=['user','namear','nameen','country']
class SimpleRoomSerializer(serializers.ModelSerializer):
      class Meta :
            model=Room
            fields=['nameen','namear','descar','descen','roombeds','roomguests']     




class ManualReservationSerilaizer(serializers.ModelSerializer):
        
        def __init__(self, instance=None, data=..., **kwargs):
              super().__init__(instance, data, **kwargs)
        hotel=SimpleHotelSerializer()
        room=SimpleRoomSerializer()
        bedoption=BedoptionSerializer()
        guestoption=GuetsoptionsSerializer()
        class Meta:
            model=Manualreservations
            fields=['hotel','room','bedoption','guestoption']                            

class IconsSerializer(serializers.ModelSerializer):
      class Meta:
            model=Icon
            fields='__all__'            
class SimpleroomStopsaleserilaizer(serializers.ModelSerializer):
      class Meta:
            model=Room
            fields=['id','main','namear','nameen']     
class AddStopSaleSerializer(serializers.ModelSerializer):

      # room=SimpleroomStopsaleserilaizer(read_only=True)
      class Meta:
            model=StopSale
            fields=['room','startdate','enddate','hotel']

class ViewstopSaleSerializer(serializers.ModelSerializer):

      room=SimpleroomStopsaleserilaizer(read_only=True)
      class Meta:
            model=StopSale
            fields=['id','room','startdate','enddate','hotel']            

class PeriodsSerializer(serializers.ModelSerializer):
      class Meta:
            model=Periods
            fields='__all__'



class RateGroupserializer(serializers.ModelSerializer):
      class Meta:
            model=Groups
            fields=['name','currency']    

class RateMealplanerializer(serializers.ModelSerializer):
      class Meta:
            model=MealPlan
            fields=['nameen','namear']           
class RatePeriodserializer(serializers.ModelSerializer):
      class Meta:
            model=Periods
            fields='__all__'        
class RateRoomsrializer(serializers.ModelSerializer):
      class Meta:
            model=Room
            fields=['nameen','namear']                   

class RateSerializer(serializers.ModelSerializer):
      mealplan=RateMealplanerializer()
      period=RatePeriodserializer()
      group=RateGroupserializer()
      room=RateRoomsrializer()

      class Meta:
            model=Rate
            fields=['id','hotel','room','mealplan','group','period','netrate']         

class fixedupdateserilizer(serializers.ModelSerializer):
      val=serializers.CharField(max_length=255)
      class Meta :
            model=Update
            fields='__all__'
class UpdateDetailsSerializer(serializers.ModelSerializer):
      update=serializers.CharField(read_only=True)
      def create(self, validated_data):
            print("Create New Update Details with ")
            print(validated_data)
            query=Update.objects.filter(id=self.context['update_id']).first()
            print(query)
            
            return UpdateDetails.objects.create(update=query,**validated_data)
      class Meta:
            model=UpdateDetails
            fields=['id','period','val','update']

class relatedupdateserilizer(serializers.ModelSerializer):
      def __init__(self, instance=None, data=..., **kwargs):
            print('-------init relatedupdateserilizer')
            print(data)
            super().__init__(instance, data, **kwargs)
      # d=UpdateDetailsSerializer(many=True)

      # val=serializers.CharField(max_length=255)
     
      class Meta :
            model=UpdateDetails
            fields=['val','period','update']
            # depth=2    
class percentupdateserilizer(serializers.ModelSerializer):
      val=serializers.CharField(max_length=255)
      class Meta :
            model=Update
            fields=['val',]       

class UpdateSerializer(serializers.ModelSerializer):
      data = serializers.SerializerMethodField()
      
      def get_data(self, obj):
            print("tttttttttttttttttttttt")
            print(obj.type)
            # do your conditional logic here
            # and return appropriate result
            if obj.type=='f':
                  print("retrun fixedupdateserilizer serilizer")
                  return obj.value
            if obj.type=='r':
                  print("retrun relatedupdateserilizer serilizer")
                  query=UpdateDetails.objects.filter(update=obj.id)
                  print(query.count())
                  a=relatedupdateserilizer(data=query,many=True)
                  a.is_valid()
                  return a.data
            if obj.type=='p':
                  print("retrun percentupdateserilizer serilizer")
                  return obj.percent
            
      
      class Meta:
            model=Update
            fields=['id','mealplan','room','hotel','period','group','type','u_tupe','data','percent','value']                   



class AvailabilitydetailsSerializer(serializers.ModelSerializer):
      class Meta:
            model=AvailabilityperoiodsDetails
            fields='__all__'



class AvailabilitySerializer(serializers.ModelSerializer):
      data = serializers.SerializerMethodField()
      # def create(self, validated_data):
      #       print(validated_data)
            
      #       return super().create(validated_data)
      
      def get_data(self, obj):
            print(obj.type)
 
            if obj.type=='all':
                  print("retrun fixedupdateserilizer serilizer")
                  return obj.val
            if obj.type=='c':
                  print("retrun relatedupdateserilizer serilizer")
                  print(obj.id)
                  query=AvailabilityperoiodsDetails.objects.filter(availability=obj.id)
                  print(query.count())
                  a=AvailabilitydetailsSerializer(data=query,many=True)
                  a.is_valid()
                  return a.data

      class Meta:
            model=Availability
            fields=['id','type','val','data','room']
class SupplementSerializer(serializers.ModelSerializer):
      class Meta:
            model=Supplement
            fields='__all__'     
class UsersSerializer(serializers.ModelSerializer):
      class Meta:
            model=Users
            fields='__all__'                   


# class MySerializer(serializers.Serializer):
#     field1 = serializers.CharField()
#     field2 = serializers.CharField()
#     field3 = serializers.CharField()

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
        
#         if data.get('field1') == 'value1':
#             self.__class__ = MyDynamicSerializer
#             self.fields['dynamic_field'] = serializers.CharField()
#             data = super().to_representation(instance)
#         else:
#             self.fields.pop('dynamic_field', None)
        
#         return data

# class MyDynamicSerializer(MySerializer):
#     dynamic_field = serializers.CharField()

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['dynamic_field'] = 'Dynamic Value'
#         return data\\\
class EmailsSerilizer(serializers.ModelSerializer):
      class Meta:
          model=Emails
          fields='__all__'
class NotificationSerilizer(serializers.ModelSerializer):
      class Meta:
            model=Notification  
            field="__all__"    
class ExtraServicesSerilizer(serializers.ModelSerializer):
      class Meta:
            model=ExtraServices  
            field="__all__"                    
class AdminListHotelsSerializer(serializers.ModelSerializer):
      photos=PhotosSerializer(many=True,read_only=True)
      
      groups=GroupSerializer(many=True,read_only=True)
      rooms=RoomSerializer(many=True,read_only=True)
      rates=RateSerializer(many=True,read_only=True)
      users=UsersSerializer(many=True,read_only=True)
      periods=PeriodsSerializer(many=True,read_only=True)
      update=UpdateSerializer(many=True,read_only=True)
      emails=EmailsSerilizer(many=True,read_only=True)
      Manualreservations=ManualReservationSerilaizer(many=True,read_only=True)

      stopsale=AddStopSaleSerializer(many=True,read_only=True)
      mealplans=MealplanSerializer(many=True,read_only=True)
      Notification=NotificationSerilizer(many=True,read_only=True)
      extra_services=ExtraServicesSerilizer(many=True,read_only=True)
      Supplement=SupplementSerializer(many=True,read_only=True)
      
      class Meta:
            model=Hotel
            fields=['id','user','namear','nameen','photos','groups','phone','review','website','email','PlusCode','stopsale','periods','Manualreservations'
                    ,'mealplans','Notification','extra_services','emails','users','Supplement','rates','update','rooms',
                    'close_time','Instagram','facebook','Linked_in','twitter','sales_email',
                    'sales_phone','availabilityandrateprovider','b2b','b2c','reservation_email',
                    'reservation_phone','accounting_email','accounting_phone','logo','Category',
                    'HoteStars','country','city','location','postcode','lat','long','descar' ,'descen'
                    ,'policyen','policyar','icons','user_name','email']
      def save(self, **kwargs):
            print("serilizer save method ---------------->")
            return super().save(**kwargs)   
class SuperAdminListHotelsSerializer(serializers.ModelSerializer):
      contractAttachment=ContractAttachementSerilizer(many=True,required=False)
      photos=PhotosSerializer(many=True,required=False)
      user=serializers.CharField(read_only=True)
      def create(self, validated_data):
            print('super admin create new hotel')
            return Hotel.objects.create(user_id=self.context['userid'],**validated_data)
   
      class Meta:
            model=Hotel
            fields=['id','user','namear','nameen','phone','review','website'
                    ,'email','PlusCode','password','photos',
                  
                    'close_time','Instagram','facebook','Linked_in','twitter','sales_email',
                    'sales_phone','availabilityandrateprovider','b2b','b2c','reservation_email',
                    'reservation_phone','accounting_email','accounting_phone','logo','Category',
                    'HoteStars','country','city','location','postcode','lat','long','descar' ,'descen'
                    ,'policyen','policyar','icons','contractAttachment','user_name','email']
      def save(self, **kwargs):
            print("serilizer save method ---------------->")
            return super().save(**kwargs)      
