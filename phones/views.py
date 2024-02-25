from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = list(Phone.objects.all())
    if sort:
        if sort == 'name':
            phones.sort(key=lambda phone: phone.name)
        elif sort == 'min_price':
            phones.sort(key=lambda phone: phone.price)
        elif sort == 'max_price':
            phones.sort(key=lambda phone: phone.price, reverse=True)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    print(phone.name)
    context = {'phone': phone}
    return render(request, template, context)
