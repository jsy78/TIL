from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def main(request):
    return render(request, "reviews/main.html")


def review(request):
    reviews_ = Review.objects.all()
    context = {
        "reviews": reviews_,
    }

    return render(request, "reviews/index.html", context)


def new(request):
    return render(request, "reviews/new.html")


def create(request):
    title_ = request.POST.get("title")
    star_ = request.POST.get("star")
    content_ = request.POST.get("content")

    Review.objects.create(title=title_, content=content_, star=star_)

    return redirect("reviews:review")


def detail(request, pk):
    movie_title = Review.objects.get(id = pk)

    context = {
        'review' : movie_title,
    }
    return render(request, "reviews/detail.html", context)

def delete(request, pk):
    Review.objects.get(id = pk).delete()

    return redirect("reviews:review")

def edit(request, pk):
    edit_review = Review.objects.get(id = pk)

    context = {
        'edit_review' : edit_review,
    }

    return render(request, "reviews/edit.html", context)

def update(request, pk):
    # 업데이트를 할 애를 받아오고 id pk
    target = Review.objects.get(id = pk)
    title = request.POST.get("title")
    star = request.POST.get("star")
    content = request.POST.get("content")

    target.title = title
    target.star = star 
    target.content = content

    target.save()

    return redirect("reviews:review")
