from django.http import HttpResponse
from django.shortcuts import render
import mainapp.models as app
import random



def convert_specifications(user_string):
    '''Разбивает пользовательский ввод из админки'''
    # Пользовательские ввод должен быть вида: "Дальность%200m\r\n"
    new_text = user_string.split('\r\n')
    new_specifications = []
    for a in new_text:
        b = a.split('%')
        new_specifications.append(b)
    return new_specifications

def products_random():
    ''' Выбирает три случайных товара '''
    items = list(app.Product.objects.all())
    random_products = random.sample(items, 3) # [<Product: AGM-MS3>, <Product: AGM-AS35>, <Product: CW 15>]
    random_products_info = []
    for pr in random_products:
        info_prod = app.Product.objects.values().get(name=pr)
        manufacturer_name = app.Brand.objects.get(product=pr)
        manufacturer_url = app.Brand.objects.get(name=manufacturer_name).url_dop
        info_prod['manufacturer_name'] = manufacturer_name
        info_prod['manufacturer_url'] = manufacturer_url
        random_products_info.append(info_prod)
        
    return random_products_info
        
def product_selected(prod_urls):
    ''' Выбирает продукты по переданному списку url'ов '''
    
    products = []
    for each in prod_urls:
        product_info = app.Product.objects.values().get(url_dop=each)
        manufacturer_name = app.Brand.objects.get(product=product_info['id']) # здесь только id можно писать?
        manufacturer_url = app.Brand.objects.get(name=manufacturer_name).url_dop
        product_info['manufacturer_name'] = manufacturer_name
        product_info['manufacturer_url'] = manufacturer_url    
        products.append(product_info)
    
    return products
    
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

def add_manufacturer_to_product(select_products):
    ''' Добавляет бренды к продуктам '''
    print (select_products)


def search(request):
    
    context = context_gen()
    
    # приходит ввод пользователя из поля search в base.html
    search_user = request.GET.get('search_user')
    
    # находит продукты по совпадению в имени / артикуле / бренде
    search_products =   app.Product.objects.filter(name__icontains=search_user) | \
                        app.Product.objects.filter(code__icontains=search_user) | \
                        app.Product.objects.filter(manufacturer__name__icontains=search_user)

    # заменяет все продуты в контексте на те, которые соответствуют поиску
    context['products'] = search_products 
    
    # считает сколько товаров найдено
    context['search_count'] = context['products'].count()
    
    # запрос пользователя
    context['search_by_user'] = search_user
    
    # Добавляем в словарь с продуктами производителя и ссылку на него
    for each in context['products']:
        manufacturer_name = app.Brand.objects.get(product=each.id) # здесь только id можно писать?
        manufacturer_url = app.Brand.objects.get(name=manufacturer_name).url_dop
        each.manufacturer_name = manufacturer_name
        each.manufacturer_url = manufacturer_url  
    
    return render(request, 'mainapp/search.html', context=context)




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
    
    context['products'] = app.Product.objects.values().all()
    context['products_choice'] = products_random()
    context['products_selected'] = product_selected(['agmas35', 'agmms3']) # сюда вписываем url продуктов, которые хотим там видеть
    
    # Добавляем в словарь с продуктами производителя и ссылку на него
    for each in context['products']:

        manufacturer_name = app.Brand.objects.get(product=each['id']) # здесь только id можно писать?
        manufacturer_url = app.Brand.objects.get(name=manufacturer_name).url_dop
        each['manufacturer_name'] = manufacturer_name
        each['manufacturer_url'] = manufacturer_url   

    
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