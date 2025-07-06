from django.contrib import admin
from .models import AdminProfile
# Register your models here.
@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'access_level')
    search_fields = ('user__username', 'access_level')
    list_filter = ('access_level',)
    