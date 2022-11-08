from django.shortcuts import render
from django.http import HttpResponse

tasks = ['foo','bar','baz']
posts = [
    {
        'author': 'Anna',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': 'August 10, 2020'
    },
    {
        'author': 'Jane',
        'title': 'Blog post 2',
        'content': 'First post content',
        'date': 'August 1, 2020'
    }
]
# Create your views here.
def index(request):
    return render(request,'blog/index.html',{'tasks':tasks,
                                              'posts':posts})
def about(request):
    return HttpResponse('<p>This is about page</p>')
def greet(request,name):
    return HttpResponse(f'<p>Hello { name.capitalize() }!</p>')
def users(request,id):
    return HttpResponse(f'<p>Hello User, { id }</p>')