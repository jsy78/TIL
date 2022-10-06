from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies_ = Movie.objects.order_by("-pk")
    context = {"movies": movies_}

    return render(request, "movies/index.html", context)


def detail(request, pk):
    movie_ = Movie.objects.get(pk=pk)
    context = {"movie": movie_}

    return render(request, "movies/detail.html", context)


def create(request):
    if request.method == "POST":
        movie_form_ = MovieForm(request.POST)
        if movie_form_.is_valid():
            movie_form_.save()

            return redirect("movies:index")

    else:
        movie_form_ = MovieForm()

    context = {"movie_form": movie_form_}

    return render(request, "movies/create.html", context)


def update(request, pk):
    movie_ = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_form_ = MovieForm(request.POST, instance=movie_)
        if movie_form_.is_valid():
            movie_form_.save()

            return redirect("movies:index")

    else:
        movie_form_ = MovieForm(instance=movie_)

    context = {"movie": movie_, "movie_form": movie_form_}

    return render(request, "movies/update.html", context)


def delete(request, pk):
    movie_ = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_.delete()

        return redirect("movies:index")
    else:
        context = {"movie": movie_}

        return render(request, "movies/detail.html", context)
