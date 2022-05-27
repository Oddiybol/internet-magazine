from django.contrib import admin
from market.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','message','sent_at']
    search_fields = ['name','email','address','message','sent_at']
    list_editable = ['address']
admin.site.register(User, UserAdmin)