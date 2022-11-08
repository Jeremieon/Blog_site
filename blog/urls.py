from django.urls import path
from . import views
from users import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('<str:name>/', views.greet, name='greet'),
    path('user/<int:id>/', views.users, name='number'),


]