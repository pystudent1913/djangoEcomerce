from django.contrib import admin
from products.models import Product, ProductImage


# para este sitio 
# user123
# admin123

class ProductImageInLine(admin.TabularInline):
    model = ProductImage



# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",) } 
    inlines = [
        ProductImageInLine
    ]


# Registramos 
admin.site.register(Product, ProductAdmin)
