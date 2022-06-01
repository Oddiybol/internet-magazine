from django.contrib import admin
from market.models import User
from market.models import Category, Product

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','message','sent_at']
    search_fields = ['name','email','address','message','sent_at']
    list_editable = ['address']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

