from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('brandpage/<str:brand_name>', views.brandpage, name='brandpage'),
    path('brands', views.brands, name='brands'),
    path('contacts', views.contacts, name='contacts'),
    path('catalog', views.catalog, name='catalog'),
    path('faq', views.faq, name='faq'),
    path('product/<str:product_name>', views.product, name='product'),
      
]