from django.contrib import admin
from .models import Contact, NewsletterSubscription
# Register your models here.

# Register your models here.
admin.site.site_header = 'OCE-MARKT'
admin.site.index_title = 'OCE-MARKT Admin'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ['contact_name', 'email',
                    'subject', 'created_at', 'updated_at']


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']
