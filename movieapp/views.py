from django.shortcuts import render, redirect

from .form import Movieform
from .models import Movie


# Create your views here.
def demo(request):
    movie = Movie.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['img']

        movie = Movie(name=name, desc=desc, year=year, img=image)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html', {'movie': movie})
