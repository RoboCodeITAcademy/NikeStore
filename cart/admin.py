from django.contrib import admin
from .models import Cart,CartProduct
# Register your models here.
@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [ 'total_quantity', 'total_price']