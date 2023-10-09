from django.shortcuts import render, get_object_or_404
from . models import Product

# Create your views here.

def index(request):
    return render(request,'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html',{'products':products})

def product_detail(request, id):
    products = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html',{'products':products}) 

