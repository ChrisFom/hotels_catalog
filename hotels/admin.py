from django.contrib import admin
from .models import City, Hotel


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone', 'city')


admin.site.register(City, CityAdmin)
admin.site.register(Hotel)
