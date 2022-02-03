from django.contrib import admin
from .models import Services

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'edited')

admin.site.register(Services, ServicesAdmin)