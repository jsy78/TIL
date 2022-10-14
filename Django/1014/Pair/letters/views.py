from django.shortcuts import render, redirect
from .models import CustomLetters
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomLettersForm

# Create your views here.
@login_required
def index(request):
    letters = CustomLetters.objects.filter(recipient_id=request.user.id, garbage=False).order_by(
        "-created_at"
    )
    context = {
        "letters": letters,
    }
    return render(request, "letters/index.html", context)


@login_required
def email_send(request):
    form = CustomLettersForm(request.POST or None)
    to_info = get_user_model().objects.get(pk=request.user.id)
    if form.is_valid():
        from_info = get_user_model().objects.filter(email=request.POST["to_email"])
        for i in from_info:
            temp = form.save(commit=False)
            temp.recipient_id = i.id
            temp.from_name = to_info.username
            temp.from_email = to_info.email
            temp.save()
        return redirect("letters:index")
    context = {
        "form": form,
    }
    return render(request, "letters/email_send.html", context)


@login_required
def click_email_send(request, pk):
    from_info = get_user_model().objects.get(pk=pk)
    form = CustomLettersForm(request.POST or None, initial={"to_email": from_info.email})
    to_info = get_user_model().objects.get(pk=request.user.id)
    if form.is_valid():
        from_info = get_user_model().objects.filter(email=request.POST["to_email"])
        for i in from_info:
            temp = form.save(commit=False)
            temp.recipient_id = i.id
            temp.from_name = to_info.username
            temp.from_email = to_info.email
            temp.save()
        return redirect("letters:index")
    context = {
        "form": form,
    }
    return render(request, "letters/email_send.html", context)


@login_required
def email_detail(request, pk):
    letter = CustomLetters.objects.get(pk=pk)
    if not letter.read:
        letter.read = True
        letter.save()
    context = {
        "letter": letter,
    }
    return render(request, "letters/email_detail.html", context)


@login_required
def trash_throw_away(request, pk):
    letter = CustomLetters.objects.get(pk=pk)
    letter.garbage = True
    letter.save()
    return redirect("letters:index")


@login_required
def trash_return(request, pk):
    letter = CustomLetters.objects.get(pk=pk)
    letter.garbage = False
    letter.save()
    return redirect("letters:trash_can")


@login_required
def trash_can(request):
    trash_letters = CustomLetters.objects.filter(
        recipient_id=request.user.id, garbage=True
    ).order_by("-created_at")
    context = {
        "letters": trash_letters,
    }
    return render(request, "letters/trash_can.html", context)


@login_required
def delete(request, pk):
    letter = CustomLetters.objects.get(pk=pk)
    letter.delete()
    return redirect("letters:trash_can")


@login_required
def important_check(request, pk):
    letter = CustomLetters.objects.get(pk=pk)
    letter.important = True
    letter.save()
    return redirect("letters:index")


@login_required
def important_return(request, pk):
    letter = CustomLetters.objects.get(pk=pk)
    letter.important = False
    letter.save()
    return redirect("letters:index")


@login_required
def important(request):
    important_letters = CustomLetters.objects.filter(
        recipient_id=request.user.id, garbage=False, important=True
    ).order_by("-created_at")
    context = {
        "letters": important_letters,
    }
    return render(request, "letters/important.html", context)


@login_required
def send_can(request):
    letters = CustomLetters.objects.filter(from_name=request.user).order_by("-created_at")
    context = {
        "letters": letters,
    }
    return render(request, "letters/send_can.html", context)
