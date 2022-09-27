from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.GET.get('ball'))
    # ball = request.GET.get('ball')
    # context = {
    #   'name': ball,
    # }

    return render(request, "pong.html", {"name": request.GET.get("ball")})
