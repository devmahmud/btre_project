from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')

        #check if already inquired
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing")
                return redirect('listing',listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,phone=phone, message=message, user_id=user_id)
        contact.save()

        # sending email
        send_mail(
            'Property listing inquiry',
            'There has been an inquiry for '+ listing +'. Sign into the admin panel for more info',
            'expelmahmud@gmail.com',
            ['alam15-5563@diu.edu.bd',realtor_email,],
            fail_silently = False
        )
        messages.success(request, "Your request has been submitted, A realtor will get back to you soon")

        return redirect('listing',listing_id)
        