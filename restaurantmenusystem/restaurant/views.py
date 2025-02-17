from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView
from restaurant.models import MenuItem,Menu


# Create your views here.
class Home(TemplateView):
    template_name="home.html"

class Addmenuitem(CreateView):
    template_name="addmenuitem.html"
    model=MenuItem
    fields=['name','price','menu','is_vegetarian']
    success_url=reverse_lazy('home')

def menuview(request,i):
    b=Menu.objects.get(id=i)
    context={'key':b}
    return render(request,'menuview.html',context)

class Update(UpdateView):
    model = MenuItem
    template_name = 'update.html'
    fields = ['price']
    success_url = reverse_lazy('home')

class Menulist(ListView):
    model=Menu
    template_name='list.html'
    context_object_name='m'

