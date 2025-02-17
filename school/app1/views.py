from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,View

from app1.models import School,Student
from django.urls import reverse_lazy

from app1.forms import Schoolform
# Create your views here.
class Home(TemplateView):
    template_name="home.html"

class AddSchool(CreateView):
    model=School
    template_name="addschool.html"
    # fields=['name','location','principal']
    form_class=Schoolform
    success_url = reverse_lazy('home')

class AddStudent(CreateView):
    model = Student
    template_name = "addstudent.html"
    fields = ['name','age','school']
    success_url = reverse_lazy('home')

class Schoollist(ListView):
    model=School
    template_name="schoollist.html"
    context_object_name="key"

class Details(DetailView):
    model=School
    template_name="details.html"
    context_object_name ="k"

class Studentlist(ListView):
    model=Student
    template_name="studentlist.html"
    context_object_name = "n"

    def get_queryset(self):
        qs=super().get_queryset()
        queryset=qs.filter(age__gt=20 )
        return queryset

    def get_context_data(self):
        context=super().get_context_data()
        context['name']='Arun'
        context['school']=School.objects.all()
        return context

from app1.forms import Password
class Register(CreateView):
    model=User
    # fields=['username','password','email','first_name','last_name']
    form_class=Password
    template_name="register.html"
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        e=form.cleaned_data['email']
        f=form.cleaned_data['first_name']
        l=form.cleaned_data['last_name']
        u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
        u.save()
        return redirect('home')

from django.contrib.auth.views import LoginView
class Login(LoginView):
    template_name="login.html"

from django.contrib.auth import logout
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
