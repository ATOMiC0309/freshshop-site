from django.contrib import admin

# Register your models here.
from .models import Category, Product, Review
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'created')

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price', 'quantity', 'get_image')

    prepopulated_fields = {'slug': ('name', 'category', 'price')}

    def get_image(self, product):
        if product.image:
            url = product.image.url
        else:
            url = "https://cdni.iconscout.com/illustration/premium/thumb/result-not-found-7304098-5974964.png?f=webp"
        return mark_safe(f'<a href="{url}" target="_blank"><img src="{url}" alt="not image" width="80px"></a>')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'product', 'text', 'added')
