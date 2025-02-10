from audioop import reverse

from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView
from shop.models import Category
from django.contrib.auth.models import User
from django.contrib import messages

from shop.models import Product


# Create your views here.
class Home(ListView):
    model=Category
    context_object_name ='key'
    template_name="category.html"

class CategoryDetails(DetailView):
    model=Category
    template_name="categorydetails.html"
    context_object_name="k"

class ProductDetails(DetailView):
    model=Product
    template_name='productdetails.html'
    context_object_name = 'n'

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        k=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
        k.save()
        return redirect('shop:login')
    return render(request,'register.html')

def user_login(request):
    if request.method== "POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request, user)
            return redirect('shop:category')

        else:
            messages.error(request,"Invalid User Credentials")

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:category')

class AddCategories(CreateView):
    model=Category
    fields=['name','image','description']
    template_name='addcategories.html'
    success_url=reverse_lazy('shop:category')


class AddProducts(CreateView):
    model=Product
    fields=['name','image','stock','description','price','category']
    template_name='addproducts.html'
    success_url=reverse_lazy('shop:category')

class AddStock(UpdateView):
    template_name='addstock.html'
    model=Product
    fields=['stock']
    # success_url = reverse_lazy('shop:category')
    def get_success_url(self):
        return reverse_lazy('shop:productdetails',kwargs={'pk':self.object.id})









