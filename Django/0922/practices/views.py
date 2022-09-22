from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def template(request) :
    _number = 1
    _numbers = [1, 2, 3, 4, 5]
    context = {
        'number' : _number,
        'numbers' : _numbers,
    }

    return render(request, 'template.html', context)

def dinner(request) : 
    _menus = ['갈비', '곱창', '국밥', '돈까스', '볶음밥', '오믈렛', '족발', '짜장면', '초밥', '치킨', '피자', '불고기']
    context = {
        'menus' : _menus,
    }
    
    return render(request, 'dinner.html', context)

def lotto(request) :
    return render(request, 'lotto.html')

