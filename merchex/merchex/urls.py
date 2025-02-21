from django.contrib import admin
from django.urls import path,re_path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("bands/", views.band_list, name='band-list'),
    path("bands/<int:id>/", views.band_detail, name='band-detail'),
    path("bands/add/", views.band_create, name="band_create"),
    path("bands/<int:id>/update/", views.band_update, name="band_update"),
    path("bands/<int:id>/delete/", views.band_delete, name="band_delete"),
    
    path("listings/",views.listing, name='all-lists'),
    path("listings/<int:id>/",views.listing_details,name='list-detail'),
    path("listings/add/", views.create_list, name="create_listing"),
    path("listings/<int:id>/update/", views.listing_update, name="listing_update"),
    path("listings/<int:id>/delete", views.lising_delete, name="lising_delete"),
    
    path("about-us/", views.about, name='about'),
    path("contact-us/",views.contact, name='contact'),
    path("email/",views.emailSend,name='email-sent'),
    
    # re_path(r'^.*$',views.errorpage)
]