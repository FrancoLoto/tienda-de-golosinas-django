from django.contrib import admin
from .models import Cart, CartItem


class CartAadmin(admin.ModelAdmin):

    list_display = ('cart_id', 'date_added')

class CartItemAadmin(admin.ModelAdmin):

    list_display = ('product', 'cart', 'quantity', 'is_active')


admin.site.register(Cart, CartAadmin)
admin.site.register(CartItem, CartItemAadmin)



