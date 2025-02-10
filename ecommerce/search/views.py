from django.db.models import Q
from django.shortcuts import render
from shop.models import Product
# Create your views here.

def searchnow(request):
    p=None
    query=""
    if request.method== "POST":
        query=request.POST['q']
        if query:
            p=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'key':p})
