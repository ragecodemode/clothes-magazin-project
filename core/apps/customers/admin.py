from django.contrib import admin

from core.apps.customers.models.customers import Customer
from core.apps.customers.models.favorites import Favorite


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at')
    search_fields = ('phone', 'email',)
    
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display= ('id', 'customer', 'product')
    list_select_related = ('customer', 'product')