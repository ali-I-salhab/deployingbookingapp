from djoser.serializers import UserCreateSerializer
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

class CustomSerilizer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        
    
        fields =   (
            'email',
        'username',
        "phone","country",
       

            "password","is_staff",'first_name',"last_name","is_active","id"
        )

