from django.contrib import admin
import mainapp.models as app

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'html_class_name')
admin.site.register(app.Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation', 'country', 'url_dop')
admin.site.register(app.Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'on_main_page', 'url_dop')
admin.site.register(app.Product, ProductAdmin)

class FeedFilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'presentation')
admin.site.register(app.FeedFiles, FeedFilesAdmin)