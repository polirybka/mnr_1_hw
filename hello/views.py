from django.shortcuts import render
from .forms import SeatNumberForm
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage



def home(request):
    return render(request, "hello/home.html")

def kvest1(request):
    return render(request, "hello/kvest/kvest1.html")
def kvest2(request):
    return render(request, "hello/kvest/kvest2.html")
    
def list(request):
    template = 'hello/list.html'
    context = {
        'my': {
            'name': 'Барыбина Полина Олеговна',
            'phone': '+79152622260',
            'mail': 'pobarybina@edu.hse.ru',
            'img': '../static/hello/me.png'
        },
        'program': {
            'name': 'Дизайн',
            'description': 'дизайнеры очень грустные',
            'ruk': {
                'name': 'Захар День',
                'mail': 'zharitonov@hse.ru',
                'img' :'https://design.hse.ru/system/tt_people/photos/000/000/125/large/Zahar_Den.jpg'
            },
            'men': {
                'name': 'Вадим Булгаков',
                'mail': 'vbulgakov@hse.ru',
                'img' :'https://design.hse.ru/system/tt_people/card_images/000/000/637/large/%D0%91%D1%83%D0%BB%D0%B3%D0%B0%D0%BA%D0%BE%D0%B2.jpg'
            }
        },
        'friend_1': {
            'name': 'Колодина Настя',
            'phone': '+77777777777',
            'mail': 'akolodina@edu.hse.ru',
            'img': 'https://i.pinimg.com/564x/b9/d6/3a/b9d63acbe72f9a9075086434afc6dd5c.jpg'
        },
        'friend_2': {
            'name': 'Климова Дарья',
            'phone': '+88888888888',
            'mail': 'dklimova@edu.hse.ru',
            'img': 'https://i.pinimg.com/564x/4a/63/6b/4a636b324008eefe135bc940a9758257.jpg'
        },
    }
    return render(request, template, context)

def task(request):
    if request.method == 'POST':
        form = SeatNumberForm(request.POST)
        if form.is_valid():
            seat_number = form.cleaned_data['seat_number']

            if 37 <= seat_number <= 54:
                result = 'Боковое место в плацкартном вагоне'
            elif 1 <= seat_number <= 38:
                result = 'Купейное место в плацкартном вагоне'
            else:
                result = 'Номер места вне допустимого диапазона'

            if 1 <= seat_number <= 54:
                if seat_number % 2 == 0:
                    result += ', верхнее'
                else:
                    result += ', нижнее'
            else:
                result = 'Номер места вне допустимого диапазона'
        else:
            result = None
    else:
        form = SeatNumberForm()
        result = None

    return render(request, 'hello/task.html', {'form': form, 'result': result})

def about(request):
    return render(request, "hello/about.html")



def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    # return HttpResponse(content)
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
