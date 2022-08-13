from django.contrib import admin
from django.urls import path
from .models import *
from .forms import CsvImportForm
from django.shortcuts import render


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Color._meta.fields]

    class Meta:
        model = Color


admin.site.register(Color, ColorAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Type._meta.fields]

    class Meta:
        model = Type


admin.site.register(Type, TypeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class TextileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Textile._meta.fields]

    class Meta:
        model = Textile


admin.site.register(Textile, TextileAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]

    class Meta:
        model = Country


admin.site.register(Country, CountryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'category']
    list_filter = ['type', 'category']
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)


class BaguetteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'material', 'color']
    list_filter = ['material', 'color']

    class Meta:
        model = Baguette


admin.site.register(Baguette, BaguetteAdmin)


class BaguetteColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BaguetteColor._meta.fields]

    class Meta:
        model = BaguetteColor


admin.site.register(BaguetteColor, BaguetteColorAdmin)


class BaguetteMaterialAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BaguetteMaterial._meta.fields]

    class Meta:
        model = BaguetteMaterial


admin.site.register(BaguetteMaterial, BaguetteMaterialAdmin)