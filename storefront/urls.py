"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import debug_toolbar
# customize admin
admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

from django.urls import path
from core.views import security_txt
urlpatterns = [



    # ...
    path(".well-known/assetlinks.json", security_txt),

    path("auth/", include("djoser.social.urls")),

path('admin/', admin.site.urls),
   

    path('__debug__/', include(debug_toolbar.urls)),    
      path('auth/', include('djoser.urls'))

      ,path('auth/', include('djoser.urls.jwt'))   ,
              path('booking/', include('booking.urls')),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
