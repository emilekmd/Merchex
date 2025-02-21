from django.shortcuts import render,redirect
from .models import Band,Listing
from .forms import ContactUsForm,BandsForm,ListForm
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

def band_update(request,id):
    band = Band.objects.get(id=id)
    
    if request.method == "POST":
        form = BandsForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail',band.id)
    else:
        form = BandsForm(instance=band)
    
    return render(request,'listings/band_update.html',{'form':form})

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

def listing_update(request,id):
    listing = Listing.objects.get(id=id)    
    
    if request.method == 'POST':
        form = ListForm(request.POST,instance=listing)
        form.save()
        return redirect ('list-detail',listing.id)
    else:
        form = ListForm(instance=listing)
    return render (request,'listings/listing_update.html',{'form':form})

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

def band_create(request):

    if request.method == "POST":
        band_form = BandsForm(request.POST)
        if band_form.is_valid():
            band=band_form.save()
            return redirect('band-detail',band.id)
    else:
        band_form = BandsForm()
    return render(request,"listings/bands_create.html",{'band_form':band_form})

def create_list(request):
    if request.method=="POST":
        form=ListForm(request.POST)
        if form.is_valid:
            list = form.save()
            return redirect ('list-detail',list.id)
    else:
        form=ListForm()
    return render(request,'listings/create_list.html',{"form":form})

def errorpage(request):
    return render(request,"listings/404.html")