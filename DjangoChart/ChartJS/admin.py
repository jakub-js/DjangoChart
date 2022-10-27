from django.contrib import admin
from .models import Chart


# Register your models here.
# admin.site.register(Chart)

@admin.register(Chart)  # dekorowanie
class ChartAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['title']
    search_fields = ['title']
