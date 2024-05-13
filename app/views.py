from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    products= Product.objects.all()
    context={
        'products': products
    }
    return render(request,'home.html',context)
def Detail(request,id):
    #lọc dữ liệu phương thức get và phương thức filter
    #phương thức get
    product=Product.objects.get(id=id)
    context={
        'product': product
    }
    return render(request,'detail.html',context)