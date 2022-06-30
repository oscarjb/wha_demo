from re import search
from django.contrib import admin
from wha_products.models import Company, Products, Audios

# Register your models here.

class Company_admin(admin.ModelAdmin):
    list_display = ("name_company", 
                    "email",
                    "telephone_number",
                    "address",
                    "country",
                    "products",
                    "username_company")
    
    search_fields = ("name_company", "email")

    def products(self, obj):
        return ", ".join([
            p.name_product for p in obj.product.all()
        ])
        return obj.product.name_product

    def username_company(self, obj):
        return obj.user_company.id

class Products_admin(admin.ModelAdmin):
    list_display = ("name_product",
                    "description",)


class Audio_admin(admin.ModelAdmin):
    list_display = ("audio_path",
                    "get_product",)

    def get_product(self, obj):
        return obj.product.name_product
        

admin.site.register(Company, Company_admin,)
admin.site.register(Products, Products_admin,)
admin.site.register(Audios, Audio_admin,)