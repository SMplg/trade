from django.http import HttpResponse
from django.shortcuts import render
import mainapp.models as app


def context_gen():
    ''' Генерация значений из БД '''

    context = {}
    
    context['brands'] = app.Brand.objects.all()
    context['company'] = {
        'company_email':'sales@trade.ru',
        'company_phone':'8(861)2002010',
        'company_phone_for_html': 78612002010,
        'company_adress':'Краснодар, ул. Фрунзе 22/1'  
    }
    
    return context

def index(request):
    context = context_gen()
    return render(request, 'mainapp/index.html', context=context)

def aboutus(request):
    context = context_gen()
    return render(request, 'mainapp/aboutus.html', context=context)

def contacts(request):
    context = context_gen()
    return render(request, 'mainapp/contacts.html', context=context)

def brands(request):
    context = context_gen()
    return render(request, 'mainapp/brands.html', context=context)

def catalog(request):
    context = context_gen()
    return render(request, 'mainapp/catalog.html', context=context)

def product(request):
    context = context_gen()
    return render(request, 'mainapp/product.html', context=context)

def faq(request):
    context = context_gen()
    return render(request, 'mainapp/faq.html', context=context)

def brandpage(request, brand_name):
    
    context = context_gen()
    
    # все значения Бренда
    context['brand'] = app.Brand.objects.values().get(url_dop=brand_name)
    # найти id бренда, для определения категорий
    brand_id = context['brand']['id']
    # категории бренда
    context['categories'] = app.Category.objects.filter(brand=brand_id)
 
    return render(request, 'mainapp/brandpage.html', context=context)