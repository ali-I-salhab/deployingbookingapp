from .models import Hotel,HotelImages,Room
from .serializers import HotelSerializer,imagesSerializer,RoomSerializer
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

class Hotelviewset(CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin,RetrieveModelMixin,GenericViewSet):
    
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer
    parser_classes = (MultiPartParser, FormParser)

    
    # def update(self, request, *args, **kwargs):
    #     print('update')
    #     print(kwargs)
    #     print(args)
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)


    #     return Response(HotelSerializer(instance.parent).data)
      

    def create(self, request, *args, **kwargs):
        print("---------------------------")

        print(request)
        print("---------------------------")
        print(kwargs)
        print("---------------------------")
        print(args)

        return super().create(request, *args, **kwargs)
class HotelImagesViewSet(ModelViewSet):
    serializer_class = imagesSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=HotelImages.objects.all()    
# class ProductsViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     parser_classes = (MultiPartParser, FormParser)
    
    
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_class = ProductFilter
#     search_fields = ['name', 'description']
#     ordering_fields = ['old_price']
#     pagination_class = PageNumberPagination



# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer
    
#     def get_queryset(self):
#          return Review.objects.filter(product_id=self.kwargs["product_pk"])
    
#     def get_serializer_context(self):
#         return {"product_id": self.kwargs["product_pk"]}    

class RoomViewset(CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin,RetrieveModelMixin,GenericViewSet):
    
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
