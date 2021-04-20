from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model',
                    'year', 'body_style', 'fuel_type', 'is_featured')

    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'color',
                     'fuel_type', 'model', 'body_style',)
    list_filter = ('city', 'fuel_type', 'body_style', 'model')

    def thumbnail(self, objcet):
        return format_html('<img src = "{}" width="40" style= "border-radius:50px" />'.format(objcet.car_photo.url))

    thumbnail.short_description = "Car image"


admin.site.register(Car, CarAdmin)
