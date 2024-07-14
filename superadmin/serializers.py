
from rest_framework import serializers

from superadmin.models import Hotel,HotelImages,Room
class imagesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model=HotelImages
        fields=['id','image']     




class RoomSerializer(serializers.ModelSerializer):
    class Meta:
         model=Room
         fields='__all__'

        

class HotelSerializer(serializers.ModelSerializer):
     photos = serializers.SerializerMethodField()

     def get_photos(self,obj:Hotel):
     #    print("obj is")
     #    print(obj.id)
     
        photos = HotelImages.objects.filter(Hotel=obj)
        print('photos is ---')
        print(photos)

        return imagesSerializer(photos, many=True, read_only=False).data
     images=imagesSerializer(many=True,read_only=True)
     uploaded_images= serializers.ListField(required=False,
        
        child = serializers.ImageField(max_length = 1000000, required=False,allow_empty_file = True, use_url = False),
      write_only=True)

     def create(self, validated_data):
        uploaded_images=validated_data.pop('uploaded_images')

        print(uploaded_images)
        hotel=Hotel.objects.create(**validated_data)
        print(hotel)
        for image in uploaded_images:
            HotelImages.objects.create(Hotel=hotel,image=image)

        return hotel  

  
  
     class Meta:
        model=Hotel
        fields=['id','photos','name','country','city','phonenumber','Googlereviewnumber','website','email','facebookaccount','verticalline','horizontalline','images','uploaded_images']

        
