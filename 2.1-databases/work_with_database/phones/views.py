from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    list_phones = Phone.objects.all()
    if sort == 'name':
        list_phones = list_phones.order_by('name')
    elif sort == 'min_price':
        list_phones = list_phones.order_by('price')
    elif sort == 'max_price':
        list_phones = list_phones.order_by('-price')
    context = {
        'phones': list_phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
