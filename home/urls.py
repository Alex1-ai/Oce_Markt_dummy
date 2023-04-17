from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # contact page
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter'),

    #path('reviewForm/', views.reviewForm, name='reviewForm'),
    # path("review/", views.review, name="review")
]
