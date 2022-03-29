from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }

    sort = request.GET.get('sort')
    if sort:
        phones = Phone.objects.order_by(SORT_MAP[sort])
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}

    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug = slug)
    context = {'phone': phone}

    return render(request, template, context)

# def show_catalog(request):
#     template = 'catalog.html'
#
#     if 'sort' in request.GET:
#         if request.GET['sort'] == 'name':
#             phones = Phone.objects.order_by('name')
#         elif request.GET['sort'] == 'min_price':
#             phones = Phone.objects.order_by('price')
#         elif request.GET['sort'] == 'max_price':
#             phones = Phone.objects.order_by('-price')
#         else:
#             phones = Phone.objects.all()
#
#     else:
#         phones = Phone.objects.all()
#
#     context = {'phones': phones}
#
#     return render(request, template, context)


# def show_product(request, slug):
#     template = 'product.html'
#     phone = Phone.objects.get(slug=slug)
#     context = {'phone': phone}
#
#     return render(request, template, context)

def test(request):
    phone_objects = Phone.objects.all()
    # phones = [f'{p.name}, {p.price}' for p in phone_objects]
    # HttpResponse('<br>'.join(phones))
    print(phone_objects)
    for phone in phone_objects:
        print(phone.get('price'))
    return HttpResponse(phone_objects)


