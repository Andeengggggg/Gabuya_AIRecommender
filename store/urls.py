from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('movies/add/', views.add_movie, name='add_movie'),
]
