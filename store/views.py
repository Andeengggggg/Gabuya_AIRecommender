from django.shortcuts import render, redirect
from .models import Movie  # Make sure you have a Movie model
from .forms import MovieForm  # Make sure you have a MovieForm

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'store/movies_list.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies_list')
    else:
        form = MovieForm()
    return render(request, 'store/add_movie.html', {'form': form})
