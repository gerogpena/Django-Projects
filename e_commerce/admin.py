from django.contrib import admin
from .import models

# Register your models here.

class store_manager_admin(admin.AdminSite):
    site_header = 'E-Commerce Management Administration'

store_manager_site = store_manager_admin(name='StoreManagerAdmin')

admin.site.register(models.Product)
store_manager_site.register(models.Product)

admin.site.register(models.Cart)
store_manager_site.register(models.Cart)

admin.site.register(models.CartItem)
store_manager_site.register(models.CartItem)

admin.site.register(models.Order)
store_manager_site.register(models.Order)

admin.site.register(models.OrderItem)
store_manager_site.register(models.OrderItem)

admin.site.register(models.UserProfile)
store_manager_site.register(models.UserProfile)

admin.site.register(models.Review)
store_manager_site.register(models.Review)

admin.site.register(models.Category)
store_manager_site.register(models.Category)

admin.site.register(models.ProductImage)
store_manager_site.register(models.ProductImage)