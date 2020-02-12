from django.shortcuts import render
from .models import Product
# Create your views here.
def product_details_view(request):
    obj = Product.objects.get(id=1)
    object = {
        'product':obj
    }
    return render(request, 'product/detail.html', object)