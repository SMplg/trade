from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('brands', views.brands, name='brands'),
    path('catalog', views.catalog, name='catalog'),
    path('contacts', views.contacts, name='contacts'),
    path('faq', views.faq, name='faq'),
    
    path('brandpage/<str:brand_name>', views.brandpage, name='brandpage'),
    path('product/<str:product_name>', views.product, name='product'),
    
    path('search', views.search, name='search'),
    path('filterproducts', views.filterproducts, name='filterproducts')
      
]