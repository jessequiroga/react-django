from django.shortcuts import render
from .models import Product
from .form import ProductForm
# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'product/create.html', context)

def product_details_view(request):
    obj = Product.objects.get(id=1)
    object = {
        'product':obj
    }
    return render(request, 'product/detail.html', object)