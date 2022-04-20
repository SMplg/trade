from csv import list_dialects
from django.contrib import admin
import mainapp.models as app
from django.utils.html import format_html
from django.db import models
from django.forms import TextInput, Textarea

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'html_class_name')
    search_fields = ('name',)
admin.site.register(app.Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation', 'country', 'url_dop')
    search_fields = ('name',)
admin.site.register(app.Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'on_main_page', 'url_dop')
    search_fields = ('name', 'code')
admin.site.register(app.Product, ProductAdmin)

class FeedFilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'presentation')
    search_fields = ('name', 'presentation')
admin.site.register(app.FeedFiles, FeedFilesAdmin)

class MainSettingsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # readonly_fields = ('name', 'email_sales', 'email_support', 'adress', 'phone', 'phone_html')
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size':'30'})},
    }
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
admin.site.register(app.MainSettings, MainSettingsAdmin)