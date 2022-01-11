from django.http import HttpResponse
from django.shortcuts import render


company_info = {
    'company_email':'sales@trade.ru',
    'company_phone':'8(861)2002010',
    'company_phone_for_html': 78612002010
    }

def index(request):
    return render(request, 'mainapp/index.html', context=company_info)

def aboutus(request):
    return render(request, 'mainapp/aboutus.html', context=company_info)

def contacts(request):
    return render(request, 'mainapp/contacts.html', context=company_info)

def brands(request):
    return render(request, 'mainapp/brands.html', context=company_info)

def catalog(request):
    return render(request, 'mainapp/catalog.html', context=company_info)

def product(request):
    return render(request, 'mainapp/product.html', context=company_info)

def faq(request):
    return render(request, 'mainapp/faq.html', context=company_info)

def brandpage(request):
    return render(request, 'mainapp/brandpage.html', context=company_info)