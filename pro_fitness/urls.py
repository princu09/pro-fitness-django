from django.contrib import admin
from django.urls import path, include
from fitness import urls

admin.site.site_header = "pro_fitness"
admin.site.index_title = "Welcome to pro_fitness"

urlpatterns = [
    path('siteAdminApproveByNFG/', admin.site.urls),
    path('', include('fitness.urls')),
]