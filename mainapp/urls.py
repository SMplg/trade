from django.urls import path
from . import views

urlpatterns = [
    
    # base
    path('',                views.index,        name='index'),
    path('aboutus',         views.aboutus,      name='aboutus'),
    path('brands',          views.brands,       name='brands'),
    path('catalog',         views.catalog,      name='catalog'),
    path('contacts',        views.contacts,     name='contacts'),
    path('faq',             views.faq,          name='faq'),
    
    # dinamic
    path('brandpage/<str:brand_name>', views.brandpage, name='brandpage'),
    path('product/<str:product_name>', views.product,   name='product'),
    
    # action
    path('feedback/<str:reciever>', views.feedback,     name='feedback'),
    path('search',          views.search,               name='search'),
    path('filterproducts',  views.filterproducts,       name='filterproducts'),
    # path('testfilter',      views.testfilter,           name='testfilter')
      
]