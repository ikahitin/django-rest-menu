from django.contrib import admin

from menu.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price']


admin.site.register(Product, ProductAdmin)
