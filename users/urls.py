from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.register,name='register'),

   # path('register/', include('users.urls')),
    #path('blog/', include('blog.urls')),
]
