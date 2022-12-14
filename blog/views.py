from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = "bloghome.html"


class BlogPostDetailView(DetailView):
    model = Post
    template_name = "blogpost.html"
    # context_object_name = "post" or "object"
    # You can use `context_object_name` to specify a custom name for this context


class BlogCreatePostView(CreateView):
    model = Post
    template_name = "blogcreate.html"
    fields = ["title", "author", "body"]


class BlogUpdatePostView(UpdateView):
    model = Post
    template_name = "blogcreate.html"
    fields = ["title", "body"]


class BlogDeletePostView(DeleteView):
    model = Post
    template_name = "blogdelete.html"
    success_url = reverse_lazy("bloghome")
