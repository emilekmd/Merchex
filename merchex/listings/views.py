from django.shortcuts import render,redirect
from .models import Band,Listing
from .forms import ContactUsForm
from django.core.mail import send_mail

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
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} Via merchex Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
        
    return render(request,"listings/contact.html",{"form":form})

def emailSend(request):
    return render(request,"listings/email_sent.html")