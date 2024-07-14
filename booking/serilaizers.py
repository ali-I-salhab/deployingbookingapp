from rest_framework import serializers
import re
from .models import Availability, BedOptionDetails, GroupCountries, GuestOptionDetails, Hotel, Periods, Rate,Room,Photos,MealPlan,Icon,Groups,Manualreservations,RoomBedOptions,RoomGuestoption, StopSale, Supplement, Update, UpdateDetails, Users
class ListHotelsSerializer(serializers.ModelSerializer):
      
      class Meta:
            model=Hotel
            fields='__all__'
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
                        self.validated_data['logo']=oldlogo.logo.url[6:]
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

      userchoices=Icon.objects.filter(type='b')
      my_choices = [item.name for item in userchoices]
      print("------------------->")
      print(my_choices)
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
            print(self.context.get('view'))
            
            queryset=None
            if(self.context.get('view') is not None):
                  queryset= BedOptionDetails.objects.filter(room__room=self.context.get('view').kwargs['pk'])
            return BedOptionDetailsSerializer(queryset, many=True).data

      userchoices=Icon.objects.filter(type='b')
      my_choices = [item.name for item in userchoices]
      print("------------------->")
      print(my_choices)
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
      

      userchoices=Icon.objects.filter(type='b')
      my_choices = [item.name for item in userchoices]
      name=serializers.ChoiceField(choices=my_choices)


      def create(self, validated_data):
            print('--------------------------------option id')
            print(self.context['optionid'])
      
            room=RoomBedOptions.objects.get(id=self.context['optionid'])
            return BedOptionDetails.objects.create(room=room,**validated_data)

        
      class Meta:
            model=BedOptionDetails
            fields=['id','name','number','details']

class GuestOptionDetailsSerializer(serializers.ModelSerializer):
      userchoices=Icon.objects.filter(type='g')
      my_choices = [item.name for item in userchoices]
      name=serializers.ChoiceField(choices=my_choices)


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

      userchoices=Icon.objects.filter(type='g')
      my_choices = [item.name for item in userchoices]
      print("------------------->")
      print(my_choices)
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
















class PhotosSerializer(serializers.ModelSerializer):
        class Meta:
            model=Photos
            fields='__all__'   
class MealplanlSerializer(serializers.ModelSerializer):
        class Meta:
            model=MealPlan
            fields='__all__'                                          
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
class StopSaleSerializer(serializers.ModelSerializer):

      room=SimpleroomStopsaleserilaizer()
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






class AvailabilitySerializer(serializers.ModelSerializer):
      class Meta:
            model=Availability
            fields='__all__'
class SupplementSerializer(serializers.ModelSerializer):
      class Meta:
            model=Supplement
            fields='__all__'     
class UsersSerializer(serializers.ModelSerializer):
      class Meta:
            model=Users
            fields='__all__'                   