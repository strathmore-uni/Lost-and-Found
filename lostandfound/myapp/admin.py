from django.contrib import admin
from .models import AdminProfile
# Register your models here.
@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email',)
    ordering = ('user',)

from .models import User, StudentAdmin, SecurityGuardAdmin, LostItemAdmin, FoundItemAdmin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('userID', 'email', 'password')
    search_fields = ('email',)
    ordering = ('email',)
@admin.register(StudentAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'studentEmail', 'studentName')
    search_fields = ('studentEmail', 'studentName')
    list_filter = ('course',)
    ordering = ('studentName',)
@admin.register(SecurityGuardAdmin)
class SecurityGuardAdmin(admin.ModelAdmin):
    list_display = ('guardID', 'guardEmail', 'guardName')
    search_fields = ('guardEmail', 'guardName')
    ordering = ('guardName',)
@admin.register(LostItemAdmin)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('itemID', 'itemName', 'itemDescription', 'lostDate', 'student')
    search_fields = ('itemName', 'itemDescription')
    list_filter = ('lostDate',)
    ordering = ('itemName',)
@admin.register(FoundItemAdmin)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('itemID', 'itemName', 'itemDescription', 'foundDate', 'guard', 'foundBy')
    search_fields = ('itemName', 'itemDescription')
    list_filter = ('foundDate',)
    ordering = ('itemName',)
