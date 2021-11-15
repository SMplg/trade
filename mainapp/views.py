from django.http import HttpResponse
from django.shortcuts import render


company_info = {
    'company_email':'sales@trade.ru',
    'company_phone':'8(861)2002010',
    'company_phone_for_html': 78612002010
    }

def index(request):
    return render(request, 'mainapp/index.html', context=company_info)

def contacts(request):
    return render(request, 'mainapp/contacts.html')
