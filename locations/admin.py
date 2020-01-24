from django.contrib import admin
from .models import PointModel

# Register your models here.

@admin.register(PointModel)
class PointModelAdmin(admin.ModelAdmin):
    pass
    

