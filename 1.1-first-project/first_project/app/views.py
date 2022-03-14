from datetime import datetime, timezone, timedelta
import os
import time

from django.http import HttpResponse
from django.shortcuts import render, reverse

from first_project.settings import BASE_DIR


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now(timezone(timedelta(hours=+3))).strftime('%H:%M:%S %Y-%m-%d%')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    try:
        file_list = [f for f in os.listdir('.') if os.path.isfile(f)]
        return HttpResponse(file_list)
    except:
        raise NotImplemented


# def workdir_view(request):
#     # по аналогии с `time_view`, напишите код,
#     # который возвращает список файлов в рабочей
#     # директории
#     try:
#         # path = os.getcwd()
#         # path = os.path.join(os.getcwd(), 'first_project')
#         path = BASE_DIR
#         file_list = []
#         for root, dirs, files in os.walk(path):
#             for filename in files:
#                 # file_list.append(os.path.join(f'{root}{filename}\n'))
#                 file_list.append(os.path.join(f'{filename}\n'))
#         return HttpResponse(file_list)
#     except:
#         raise NotImplemented