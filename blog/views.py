from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class BlogPageView(ListView):
    model = Post

    template_name = 'index.html'

class BlogDetailView(DetailView):
    model = Post

    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post

    template_name = 'post_new.html'
    fields ='__all__'

class BlogUpdateView(UpdateView):
    model = Post

    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
