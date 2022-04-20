from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование категории')
    html_class_name = models.CharField(max_length=50, verbose_name='Имя (english)')
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        db_table = 'CATEGORY'
    def __str__(self):
        return self.name

class FeedFiles(models.Model):
    name            = models.CharField(max_length=50, verbose_name='Имя файла')
    presentation    = models.FileField(verbose_name='Файл для загрузки', upload_to='presentation/')
    html_class_name = models.CharField(max_length=50, verbose_name='Имя (english)')
    class Meta:
        verbose_name = 'Презентацию'
        verbose_name_plural = 'Презентации'
        db_table = 'PRESENTATIONS'
    def __str__(self):
        return self.name

class Brand(models.Model):
    
    url_dop         = models.CharField(max_length=45, verbose_name='ВНИМАНИЕ! УЧИТЫВАЕТСЯ ПРИ ИНДЕКСАЦИИ! Отображаемый адрес', unique=True)
    html_class_name = models.CharField(max_length=50, verbose_name='Имя (english)')
    name            = models.CharField(verbose_name='Имя бренда', max_length=80)
    img_logo        = models.ImageField(verbose_name='Логотип бренда', upload_to='images/')
    location        = models.CharField(verbose_name='Головной офис (город)', max_length=50)
    country         = models.CharField(verbose_name='Страна', max_length=50)
    foundation      = models.PositiveIntegerField(verbose_name='Основание')
    category        = models.ManyToManyField(Category, verbose_name='Направления бренда')
    description_short   = models.TextField(verbose_name='Краткое описание')
    description_full    = models.TextField(verbose_name='Пару слов о бренде')
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        db_table = 'BRANDS'
    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    url_dop         = models.CharField(max_length=45, verbose_name='ВНИМАНИЕ! УЧИТЫВАЕТСЯ ПРИ ИНДЕКСАЦИИ! Отображаемый адрес', unique=True)
    code            = models.PositiveIntegerField(verbose_name='Артикул', unique=True)
    manufacturer    = models.ManyToManyField(Brand, verbose_name='Производитель')
    name            = models.CharField(max_length=50, verbose_name='Имя продукта')
    img_product     = models.ImageField(verbose_name='Изображение продукта', upload_to='images/')
    category        = models.ManyToManyField(Category, verbose_name='Категория')
    price           = models.IntegerField(verbose_name='Стоимость продукта')
    specifications  = models.TextField(verbose_name='Спецификации разделять символом }}')
    download_files  = models.ManyToManyField(FeedFiles, verbose_name='Выберите файлы для скачивания')
    description_short   = models.TextField(verbose_name='Краткое описание')
    description_full    = models.TextField(verbose_name='Описание')
    on_main_page    = models.BooleanField(default=False, verbose_name='Показывать на "Главной"')
            
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table = 'PRODUCTS'
    def __str__(self):
        return self.name



    
class MainSettings(models.Model):
    
    name = models.CharField(verbose_name='Настройки', max_length=45)
    
    advertising = models.TextField(verbose_name='Реклама в шапке')
    
    # phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(unique = True, verbose_name='Телефон компании', max_length=25)
    phone_html = models.IntegerField(default=170)
    adress = models.CharField(max_length=86, verbose_name='Адрес')
    email_sales = models.EmailField(max_length=254, verbose_name='Email (продажи)')
    email_support = models.EmailField(max_length=254, verbose_name='Email (поддержка)')
    
        # 'company_email':'sales@trade.ru',
        # 'company_phone':'8(861)2002010',
        # 'company_phone_for_html': 78612002010,
        # 'company_adress':'Краснодар, ул. Фрунзе 22/1'  
        
        
    class Meta:
        verbose_name = 'Hастройки'
        verbose_name_plural = 'Hастройки'
        db_table = 'MAINSETTINGS'
        
    def __str__(self):
        return self.name