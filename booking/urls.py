from django.urls import path,include
from . import views
from rest_framework_nested import routers


router=routers.DefaultRouter()
router.register('hotels',viewset=views.Hotelviewset,basename='hotels')
router.register('icons',viewset=views.IconsViewset,basename='icons')

router.register('photos',viewset=views.Photosviewset,basename='photos')
router.register('updates',viewset=views.Updatesviewset,basename='updates')
updatedetails_router= routers.NestedDefaultRouter(router, 'updates', lookup='updates')
updatedetails_router.register('details', views.UpdateDetailsviewset, basename='details')
router.register('rooms',viewset=views.Roomviewset,basename='rooms')
router.register('mealplans',viewset=views.Mealplanviewset,basename='mealplans')
router.register('groups',viewset=views.Groupviewset,basename='groups')
router.register('stopsale',viewset=views.Stopsaleviewset,basename='stopsale')
router.register('periods',viewset=views.Periodsviewset,basename='periods')
router.register('rate',viewset=views.Rateviewset,basename='rate')
router.register('availability',viewset=views.Availabilityviewset,basename='availability')
router.register('users',viewset=views.Usersviewset,basename='availability')

router.register('Supplement',viewset=views.Supplementviewset,basename='Supplement')






groupscountrie_router=routers.NestedDefaultRouter(router, 'groups', lookup='groups')
groupscountrie_router.register('countries', views.GroupCountriesViewset, basename='guests-items')

router.register('manualreservation',viewset=views.ManualReservation,basename='manualreservation')
roomrguestoption_router = routers.NestedDefaultRouter(router, 'rooms', lookup='room')
roomrguestoption_router.register('guests', views.RoomGuetsoptionsviewset, basename='guests-items')
roomGuestdetails_router= routers.NestedDefaultRouter(roomrguestoption_router, 'guests', lookup='details')
roomGuestdetails_router.register('options', views.RoomGuestoptionsDetailsviewset, basename='setails')
# -----------------------------
roombedoption_router = routers.NestedDefaultRouter(router, 'rooms', lookup='room')
roombedoption_router.register('beds', views.RoomBedoptionsviewset, basename='beds-items')
roombeddetails_router= routers.NestedDefaultRouter(roombedoption_router, 'beds', lookup='details')
roombeddetails_router.register('options', views.RoomBedoptionsDetailsviewset, basename='setails')
# _________________________________________________
urlpatterns = [
   
]
urlpatterns+= router.urls+roomrguestoption_router.urls+roombedoption_router.urls+updatedetails_router.urls+roombeddetails_router.urls+groupscountrie_router.urls+roomGuestdetails_router.urls


# router.register('products', views.ProductViewSet, basename='products')

# products_router = routers.NestedDefaultRouter(
#     router, 'products', lookup='product')
# products_router.register('reviews', views.ReviewViewSet,
#                          basename='product-reviews')
# products_router.register(
#     'images', views.ProductImageViewSet, basename='product-images')