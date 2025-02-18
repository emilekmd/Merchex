from django.shortcuts import render
from .models import Band,Listing
from django.http import HttpResponse

def hello (request):
    bands = Band.objects.all()
    return render(request,"listings/hello.html",{'bands':bands})

def about(request):
    return render (request,"listings/about.html")

def listing(request):
    listes=Listing.objects.all()
    
    return render(request,"listings/listing.html",{'listes':listes})

def contact(request):
    return render(request,"listings/contact.html")