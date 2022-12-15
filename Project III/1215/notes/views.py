from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from django.contrib.auth import get_user_model
from datetime import datetime, timezone
from .models import Received_Note, Sent_Note
from .forms import NoteForm

# Create your views here.
@login_required
@require_safe
def index(request):
    return redirect("notes:received_box")


@login_required
@require_safe
def received_box(request):
    received_notes = Received_Note.objects.filter(received_user=request.user, is_important=False, is_trash=False).order_by("-pk")
    context = {
        "notes": received_notes,
    }
    return render(request, "notes/received_box.html", context)


@login_required
@require_safe
def sent_box(request):
    sent_notes = Sent_Note.objects.filter(sent_user=request.user).order_by("-pk")
    context = {
        "notes": sent_notes,
    }
    return render(request, "notes/sent_box.html", context)


@login_required
@require_safe
def important_box(request):
    important_notes = Received_Note.objects.filter(received_user=request.user, is_important=True, is_trash=False).order_by("-pk")
    context = {
        "notes": important_notes,
    }
    return render(request, "notes/important_box.html", context)


@login_required
@require_safe
def trash_box(request):
    trash_notes = Received_Note.objects.filter(received_user=request.user, is_trash=True).order_by("-pk")
    context = {
        "notes": trash_notes,
    }
    return render(request, "notes/trash_box.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def send(request):
    
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            received_note = form.save(commit=False)
            received_note.received_user = get_user_model().objects.get(nickname=received_note.received_username)
            received_note.sent_username = request.user.nickname
            received_note.save()

            sent_note = Sent_Note()
            sent_note.sent_user = request.user
            sent_note.sent_username = request.user.nickname
            sent_note.received_username = received_note.received_username
            sent_note.title = received_note.title
            sent_note.content = received_note.content
            sent_note.received_note = received_note
            sent_note.save()

            user = get_user_model().objects.get(nickname=received_note.received_username)
            user.received_mail = int(user.received_mail) + 1
            user.save()
            
            return redirect("notes:sent_box")
    else:
        if "to" in request.GET:
            nickname = request.GET.get("to").split("&")[0]
            form = NoteForm(initial={"received_username": nickname})
        else:
            form = NoteForm()
    context = {
        "form": form,
    }
    return render(request, "notes/form.html", context)


@login_required
@require_safe
def received_note_detail(request, received_note_pk):
    received_note = Received_Note.objects.get(pk=received_note_pk)

    if request.user != received_note.received_user:
        return redirect("notes:received_box")

    if received_note.received_at_string == "읽지 않음":
        received_note.received_at = datetime.now(tz=timezone.utc)
        received_note.save()

        user = request.user
        user.received_mail = int(user.received_mail) - 1
        user.save()
        print(user.received_mail)


        try:
            sent_note = received_note.sent_note
            sent_note.received_at = received_note.received_at
            sent_note.save()
        except Received_Note.sent_note.RelatedObjectDoesNotExist:
            pass

    context = {
        "note": received_note,
    }
    return render(request, "notes/detail.html", context)


@login_required
@require_safe
def sent_note_detail(request, sent_note_pk):
    sent_note = Sent_Note.objects.get(pk=sent_note_pk)

    if request.user != sent_note.sent_user:
        return redirect("notes:sent_box")

    context = {
        "note": sent_note,
    }
    return render(request, "notes/detail.html", context)


@require_POST
def important(request, received_note_pk):
    received_note = Received_Note.objects.get(pk=received_note_pk)

    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.user != received_note.received_user:
        return redirect("notes:received_box")

    if received_note.is_important == False:
        received_note.is_important = True
    else:
        received_note.is_important = False
    received_note.save()
    return redirect("notes:received_box")


@require_POST
def trash(request, received_note_pk):
    received_note = Received_Note.objects.get(pk=received_note_pk)

    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.user != received_note.received_user:
        return redirect("notes:received_box")

    if received_note.is_trash == False:
        received_note.is_trash = True
    else:
        received_note.is_trash = False
    received_note.save()
    return redirect("notes:received_box")


@require_POST
def received_note_delete(request, received_note_pk):
    received_note = Received_Note.objects.get(pk=received_note_pk)

    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.user != received_note.received_user:
        return redirect("notes:received_box")

    if received_note.received_at_string == "읽지 않음":
        user = request.user
        user.received_mail = int(user.received_mail) - 1
        user.save()

    received_note.delete()
    return redirect("notes:trash_box")


@require_POST
def sent_note_delete(request, sent_note_pk):
    sent_note = Sent_Note.objects.get(pk=sent_note_pk)

    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if request.user != sent_note.sent_user:
        return redirect("notes:sent_box")

    sent_note.delete()
    return redirect("notes:sent_box")
