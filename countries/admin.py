from django.contrib import admin
from .models import Countries

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'uf', 'gentle')
    search_fields = ('name', 'uf', 'gentle')
    list_filter = ('name', 'uf', 'gentle')
    list_per_page = 10
    ordering = ('name', 'uf', 'gentle')
