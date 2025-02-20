from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("bands/", views.band_list, name='band-list'),
    path("bands/<int:id>/", views.band_detail, name='band-detail'),
    
    path("listings/",views.listing, name='all-lists'),
    path("listings/<int:id>",views.listing_details,name='list-detail'),
    
    path("about-us/", views.about),
    path("contact-us/",views.contact)
]