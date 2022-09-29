from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Todo

# Create your views here.
def index(request):
    todo_ = Todo.objects.all()
    context = {
        "todos": todo_,
    }

    return render(request, "todos/index.html", context)


def create(request):
    content_ = request.POST.get("content")
    priority_ = request.POST.get("priority")
    deadline_ = request.POST.get("deadline")

    if deadline_ == "":
        deadline_ = timezone.now()

    Todo.objects.create(content=content_, priority=priority_, deadline=deadline_)

    return redirect("todos:index")


def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.completed = not todo.completed
    todo.save()

    return redirect("todos:index")


def modify(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    content_ = request.POST.get("modified-content")
    priority_ = request.POST.get("modified-priority")
    deadline_ = request.POST.get("modified-deadline")

    if deadline_ == "":
        deadline_ = timezone.now()

    todo.content = content_
    todo.priority = priority_
    todo.deadline = deadline_
    todo.save()

    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")
