from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if request.POST.get("grade") == "":
            grade = 0
        else:
            grade = float(request.POST.get("grade"))
        if form.is_valid() and 0 <= grade <= 5:
            Review.objects.create(
                title=form.data.get("title"),
                content=form.data.get("content"),
                movie_name=form.data.get("movie_name"),
                grade=grade,
                user=request.user,
            )
            return redirect("reviews:index")
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.user != review.user:
        return redirect("reviews:index")

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if request.POST.get("grade") == "":
            grade = 0
        else:
            grade = float(request.POST.get("grade"))
        if form.is_valid() and 0 <= grade <= 5:
            review.title = form.data.get("title")
            review.content = form.data.get("content")
            review.movie_name = form.data.get("movie_name")
            review.grade = grade
            review.save()
            return redirect("reviews:detail", review_pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        "form": form,
        "grade": review.grade,
    }
    return render(request, "reviews/update.html", context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.user != review.user:
        return redirect("reviews:index")

    if request.method == "POST":
        if request.user == review.user:
            review.delete()
            return redirect("reviews:index")
    else:
        return redirect("reviews:detail", review_pk)
