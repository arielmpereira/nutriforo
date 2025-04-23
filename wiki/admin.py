from django.contrib import admin
from .models import Wiki

@admin.register(Wiki)
class WikiAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'creado')
    prepopulated_fields = {'slug': ('titulo',)}

