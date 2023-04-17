from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import Product, ReviewRating
from .forms import NewsletterSubscriptionForm, ContactForm
from .models import NewsletterSubscription, Contact
from app.settings import ADMIN_EMAIL
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your views here.


def home(request):

    products = Product.objects.all().filter(
        is_available=True).order_by('-modified_date')

    for product in products:
        reviews = ReviewRating.objects.filter(
            product_id=product.id, status=True)
    context = {
        'products': products,
        'reviews': reviews,

    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        # print("Entered")
        form = ContactForm(request.POST)
        # print("About to ")
        if form.is_valid():
            # print("Start")
            contact_name = form.cleaned_data['contact_name']
            # print("2")
            email = form.cleaned_data['email']
            # print("3")
            subject = form.cleaned_data['subject']
            # print("4")
            description = form.cleaned_data['description']
            # print("5")
            contact = Contact.objects.create(
                contact_name=contact_name, email=email, subject=subject, description=description)
            contact.save()
            mail_subject = 'OCE-MARKT CONTACT US MESSAGE'
            message = render_to_string(
                'accounts/contact_email.html', {
                    'user': contact_name,



                })
            to_email = ADMIN_EMAIL
            send_email = EmailMessage(
                mail_subject,
                message,
                to=[to_email]
            )
            try:
                send_email.send()
                messages.success(
                    request, "Thanks for reaching out to us, We would get back to you as soon as possible")
                return redirect('home')
            except:
                messages.error(
                    request, "Please check your internet connectiona and try again!")

        else:
            messages.error(
                request, "All the credentials are required and must be valid.")
            return redirect('contact')
    else:
        return render(request, 'contact.html')


def newsletter(request):
    # print(" this is the path", path)
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            subcriber = NewsletterSubscription.objects.create(email=email)
            subcriber.save()
            mail_subject = 'OCE-MARKT SUBSCRIPTION MESSAGE'
            message = f"Hi Admin,\nPlease some one just Subscribed to our newssletter."
            to_email = ADMIN_EMAIL
            send_email = EmailMessage(
                mail_subject,
                message,
                to=[to_email]
            )
            try:
                send_email.send()
                messages.success(
                    request, 'Thanks for subscribing to our newsletter!')

            except:
                messages.error(
                    request, "Could Not Subscribe you. Please check your internet connectiona and try again!")
            # Redirect to a success page

    return redirect(request.META.get('HTTP_REFERER'))
