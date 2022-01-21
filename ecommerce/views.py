from django.shortcuts import render
from . models import Product

# Create your views here.
def index(request):
    return render(request, 'pages/home/home.html')

def contact(request):
    content = {
        'title' : 'Contact Us'
    }
   
    
    return render(request, 'pages/contact/contact.html', content )

def product_details(request, slug):
    content = {
        'title' : 'Contact Us',
        'productData': Product.objects.get(product_slug = slug)
    }
   
    
    return render(request, 'pages/products/products-details.html', content )


