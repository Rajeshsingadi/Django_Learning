from django.contrib import admin

# Register your models here.
from .models import Something


class SomethingAdmin(admin.ModelAdmin):
    list_filter = ("title", "rating",)
    list_display = ("title", "rating",)


admin.site.register(Something)
