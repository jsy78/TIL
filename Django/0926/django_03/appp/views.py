from django.shortcuts import render


def index(request):

    return render(request, "index.html")


def print_number(request, _number):
    context = {
        # "템플릿 변수 이름" : 값
        "number": _number,
    }

    return render(request, "number.html", context)


def print_text(request):
    text = request.GET.get("_text")

    context = {
        # "템플릿 파일(.html)에서 사용할 변수 이름" : 값
        "template_text": text,
    }

    return render(request, "text.html", context)
