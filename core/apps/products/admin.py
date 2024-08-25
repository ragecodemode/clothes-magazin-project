from django.contrib import admin

from core.apps.products.models.products import Product
from core.apps.products.models.categories import Category
from core.apps.products.models.reviews import Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'discription', 'created_at', 'updated_at', 'is_active', 'category')
    inlines = (ReviewInline,)
    list_select_related = ('product')
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display= ('id', 'customer', 'product', 'rating', 'comment')
    list_select_related = ('customer', 'product')