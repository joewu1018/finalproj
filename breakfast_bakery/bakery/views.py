from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    return render(request, 'product.html')