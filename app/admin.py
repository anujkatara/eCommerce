"""admin """
from django.contrib import admin
from .models import Product, Category, Cart

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    """
    category model to the administratio site
    """
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    """
    product model to the administratio site
    """

    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
