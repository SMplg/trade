from django.contrib import admin
import mainapp.models as app

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(app.Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(app.Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(app.Product, ProductAdmin)

class FeedFilesAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(app.FeedFiles, FeedFilesAdmin)