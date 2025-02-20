from django.shortcuts import render,redirect
from .models import Band,Listing
from django.http import HttpResponse
from .forms import ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    return render(request,"listings/band_list.html",{'bands':bands})

def band_detail(request,id):
    try:
        band=Band.objects.get(id=id)
    except Band.DoesNotExist:
        return render(request,"listings/404.html")
    
    return render(request,"listings/band_details.html",{"band":band})

def about(request):
    return render (request,"listings/about.html")

def listing(request):
    listes=Listing.objects.all()
    
    return render(request,"listings/listing.html",{'listes':listes})

def listing_details (request,id):
    try:
        liste=Listing.objects.get(id=id)
    except Listing.DoesNotExist:
        return render(request,"listings/404.html")
    
    return render(request,"listings/listing_details.html",{'liste':liste,'band':liste.band})

def contact(request):
    form = ContactUsForm()
    return render(request,"listings/contact.html",{"form":form})