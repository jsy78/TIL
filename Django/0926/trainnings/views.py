from django.shortcuts import render
import random

# Create your views here.


def oddevens(request, number):
    context = {
        "number": number,
    }
    return render(request, "oddevens.html", context)


def calculate(request, num1, num2):

    if num2 == 0:
        return render(request, "zero.html")

    context = {
        "num1": num1,
        "num2": num2,
        "add": num1 + num2,
        "sub": num1 - num2,
        "mul": num1 * num2,
        "div": num1 // num2,
    }
    return render(request, "calculate.html", context)


def life(request):
    return render(request, "life.html")


def lifeShow(request):
    name = request.GET.get("name")
    ago_list = ["왕", "황제", "선비", "공룡", "말", "거북"]
    context = {"name": name, "ago": random.choice(ago_list)}

    return render(request, "life-show.html", context)


def lorem(request):
    return render(request, "lorem.html")


def loremShow(request):
    words = ["바나나", "딸기", "수박", "사과", "귤", "포도", "오렌지", "파인애플", "고구마", "밤"]
    param = int(request.GET.get("param"))
    count = int(request.GET.get("count"))
    lorem = [[] for _ in range(param)]

    for i in range(param):
        for j in range(count):
            lorem[i].append(random.choice(words))

    context = {
        "lorem": lorem,
    }
    return render(request, "lorem-show.html", context)
