from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import reviews,Comment,Favourites
from .forms import YoursReviews
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
def first(request):
    return render (request,'manhwa/first.html')

def index(request):
    if not request.user.is_authenticated:
        return redirect('first')
    manhwas= reviews.objects.all()
    context ={
        'all' : manhwas
    }
    return render (request,'manhwa/index.html',context)

def complete(request):
    if not request.user.is_authenticated:
        return redirect('first')
    finished= reviews.objects.filter(is_complete=True)
    context ={
        'completed' : finished
    }
    return render (request,'manhwa/complete.html',context)

def ongoing(request):
    if not request.user.is_authenticated:
        return redirect('first')
    continued= reviews.objects.filter(is_complete=False)
    context ={
        'goingon' : continued
    }
    return render (request,'manhwa/ongoing.html',context)

def about(request,pk):
    if not request.user.is_authenticated:
        return redirect('first')
    info= get_object_or_404(reviews,pk=pk)
    context={
        'information': info
    }
    return render (request, 'manhwa/about.html',context)

def add_reviews(request):
    if not request.user.is_authenticated:
        return redirect('first')
    if request.method == "POST":
        form=YoursReviews(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form=YoursReviews()
    context={
        "form" : form
    }
    return render(request,'manhwa/add.html',context)

def view_comments(request):
    if not request.user.is_authenticated:
        return redirect('first')
    comments = Comment.objects.all() 
    context ={
        'opinion' : comments
    }
    return render (request,'manhwa/chat.html',context)

class commentCreateView(CreateView):
    model = Comment
    fields = ['review', 'oneword', 'rating', 'description']
    success_url = reverse_lazy('chat')

    def form_valid(self, form):
        form.instance.Name=self.request.user
        return super().form_valid(form)

class commentUpdateView(UpdateView):
    model = Comment
    fields = ['oneword','rating','description']
    success_url = reverse_lazy('chat')

class commentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('chat')



def favorites(request):
    if not request.user.is_authenticated:
        return redirect('first')
    favorite = Favourites.objects.filter(user=request.user)
    context = {
        'fav' : favorite
    }
    return render(request, 'manhwa/favorites.html', context)


class favoriteCreateView(CreateView):
    model = Favourites
    fields = ['Favorite']
    success_url = reverse_lazy('favorites')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class favoriteUpdateView(UpdateView):
    model = Favourites
    fields = ['Favorite']
    success_url = reverse_lazy('favorites')

class favoriteDeleteView(DeleteView):
    model = Favourites
    success_url = reverse_lazy('favorites')