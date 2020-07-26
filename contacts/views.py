from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing_id=listing_id,listing=listing,name=name,
                          email=email,phone=phone,message=message,user_id=user_id)

        if Contact.objects.filter(listing_id=listing_id,listing=listing,name=name,
                          email=email,phone=phone,message=message,user_id=user_id).exists():
            messages.error(request, 'You have already made a request, kindly wait.')
            return redirect('/listings/' + listing_id)

        else:
            contact.save()
            # send_mail('Property Listing'
            #           'There is new entry came please check the same'
            #           'anshulrajb@gmail.com',
            #            realtor_email,
            #           fail_silently=False
            #           )
            messages.success(request, 'Your request is submitted succesfully kindly wait for the realtor reply.')
            return redirect('/listings/'+listing_id)