from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    now = timezone.now().strftime('%H')
    return render(request,'blog/index.html',{'posts':Post.objects.all(),'time': int(now)})

#all post
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']
#individual post
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #prevent users from updating other peoples post!
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post

    success_url = '/blog'

    def test_func(self): #prevent users from updating other peoples post!
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return HttpResponse('<p>Hello about</p>')