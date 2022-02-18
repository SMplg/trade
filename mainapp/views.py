from django.http import HttpResponse
from django.shortcuts import render
import mainapp.models as app

def convert_specifications(user_string):
    '''Разбивает пользовательский ввод из админки'''
    # Пользовательские ввод должен быть вида: "Дальность%200m\r\n"
    new_text = user_string.split('\r\n')
    new_specifications = []
    for a in new_text:
        b = a.split('%')
        new_specifications.append(b)
    return new_specifications

def context_gen():
    ''' Генерация значений из БД '''

    context = {}
    
    context['brands']       = app.Brand.objects.all()
    context['products']     = app.Product.objects.all()
    context['categories']   = app.Category.objects.all()
    context['company']      = {
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

def product(request, product_name):
    context = context_gen()
    context['product'] = app.Product.objects.values().get(url_dop=product_name) # все данные товара по его имени
    context['product']['specifications'] = convert_specifications(context['product']['specifications']) # парсинг спецификаций
    
    
    brands_all          = app.Brand.objects.filter(product=context['product']['id']) # находим все бренды связанные с товаром (по id товара)
    presentations_all   = app.FeedFiles.objects.filter(product=context['product']['id']) # находим все презентации связанные с товаром (по id товара)
    
    # Список перезентаций / файлов связанных с текущим продуктом
    presentations_info = []
    for p in presentations_all:
        p_name = p
        p_info = app.FeedFiles.objects.values().get(name=p_name)   
        p_info['alternative_name'] = p_info['presentation'].split("/")[-1] # вид имени /presentation/ms1.pdf меняем на ms1.pdf, убираем путь до файла из визуализации
        presentations_info.append(p_info)
    
    # Список брендов связанных с текущим продуктом
    brands_info = []
    for b in brands_all:
        b_name = b
        b_info = app.Brand.objects.values().get(name=b_name)
        brands_info.append(b_info)
        
    context['brands_per_product'] = brands_info
    context['presentations_per_product'] = presentations_info

    return render(request, 'mainapp/product.html', context=context)

def faq(request):
    context = context_gen()
    return render(request, 'mainapp/faq.html', context=context)

def brandpage(request, brand_name):
    context = context_gen()
    context['brand'] = app.Brand.objects.values().get(url_dop=brand_name)
    context['categories_filter_brand'] = app.Category.objects.filter(brand=context['brand']['id']) # id бренда в таблице Бренды
    
    # Список товаров связанных с текущим брендом
    products_all = app.Product.objects.filter(manufacturer=context['brand']['id']) # находим все товары связанные с брендом (по id бренда)
    products_info = []
    for p in products_all:
        p_name = p
        p_info = app.Product.objects.values().get(name=p_name)   
        products_info.append(p_info)
        
    context['products_per_brand'] = products_info
    
    return render(request, 'mainapp/brandpage.html', context=context)