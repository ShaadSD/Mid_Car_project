# """
# URL configuration for Car_Website project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import ProfileView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('home/',views.home,name='homepage'),
    path('/<slug:brand_slug>/',views.home,name='brand_wise_post'),
    path('car/<int:id>/',views.DetailCarView.as_view(),name='view_details'),
    path('buy_car/<int:id>/',views.buy_car,name='buy_car'),
   
     path('profile/',ProfileView.as_view(),name='profile'),
    path('add/',include('car.urls')),
    path('',include('brand.urls')),
    path('',include('Author.urls')),    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)