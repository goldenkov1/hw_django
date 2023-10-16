from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')
