from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('<str:name>/', views.greet, name='greet'),
    path('user/<int:id>/', views.users, name='number'),
    path('register/',views.users, name='number'),

]