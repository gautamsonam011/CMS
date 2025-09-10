from django.contrib import admin
from .models import Member, GroceryProducts

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("memName", "jobRole", "mobileNumber", "address", "joined_date")
# class GroceryProductsAdmin(admin.ModelAdmin):
#     list_display = ("productName")

admin.site.register(Member, MemberAdmin)     #this is admin register  
admin.site.register(GroceryProducts)