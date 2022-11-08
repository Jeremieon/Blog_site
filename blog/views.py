from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):

    return render(request,'blog/index.html',{'posts':Post.objects.all()})
def about(request):
    return HttpResponse('<p>This is about page</p>')
def greet(request,name):
    return HttpResponse(f'<p>Hello { name.capitalize() }!</p>')
def users(request,id):
    return HttpResponse(f'<p>Hello User, { id }</p>')