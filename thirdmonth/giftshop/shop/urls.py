from django.urls import path
from .views import home, contact, shop, why, testimonial



urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('shop/', shop),
    path('why/', why),
    path('testimonial/', testimonial)
    ]
