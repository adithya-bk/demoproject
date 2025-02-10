from django.shortcuts import render,redirect
from movieapp.models import Movie
from django.views.generic import ListView

# Create your views here.
# def home(request):
#     m=Movie.objects.all()
#     context={'movie':m}
#     return render(request,'home.html',context)
class Home(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie"


# def addmovie(request):
#     if(request.method=="POST"):
#         tit=request.POST['t']
#         des=request.POST['d']
#         lan=request.POST['l']
#         yea=request.POST['y']
#         img=request.FILES['i']
#         m=Movie.objects.create(title=tit,description=des,language=lan,year=yea,image=img)
#         m.save()
#
#         return redirect('home')
#
#     return render(request,'addmovie.html')
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
class AddMovie(CreateView):
    template_name="add1.html"
    fields=['title','description','language','year','image']
    model=Movie
    success_url=reverse_lazy('home')


# def details(request,i):
#     k=Movie.objects.get(id=i)
#     context={'key':k}
#     return render(request,'details.html',context)
class Details(DetailView):
    model=Movie
    template_name='details.html'
    context_object_name='key'

# def delete(request,i):
#     p=Movie.objects.get(id=i)
#     p.delete()
#     return redirect('home')

class Delete(DeleteView):
    template_name='delete.html'
    model=Movie
    success_url=reverse_lazy('home')


# def edit(request,i):
#     m=Movie.objects.get(id=i)
#     if(request.method=="POST"):
#         m.title=request.POST['t']
#         m.description=request.POST['d']
#         m.language=request.POST['l']
#         m.year=request.POST['y']
#         if(request.FILES.get('i')==None):
#             m.save()
#         else:
#             m.image=request.FILES.get('i')
#         m.save()
#         return redirect('details',m.id)
#     context={'k':m}
#     return render(request,'update.html',context)
class Edit(UpdateView):
    model=Movie
    template_name="edit.html"
    fields = ['title', 'description', 'language', 'year', 'image']
    success_url=reverse_lazy('home')



