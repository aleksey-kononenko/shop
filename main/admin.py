from django.contrib import admin
from .models import *


class SliderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Slider._meta.fields]

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)
