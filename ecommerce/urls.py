

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('contact', views.contact, name='contact' ),
    path('product-details/<slug>', views.product_details, name='product-details' ),
    
    
]
