from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contacts', views.contacts, name='contacts'),
    path('brands', views.brands, name='brands'),
    path('catalog', views.catalog, name='catalog'),
    path('product', views.product, name='product'),
    
    
]