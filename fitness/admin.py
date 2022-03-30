from django.contrib import admin
from fitness.models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Product)
@admin.register(Order)
@admin.register(Wishlist)
@admin.register(Cart)
class ModelAdmin(ImportExportModelAdmin):
       pass