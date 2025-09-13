from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Barang, UserProfile

@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):
    list_display = ['nama', 'tempat_produksi', 'halal', 'tanggal_kadaluarsa', 'kadaluarsa']
    list_filter = ['halal', 'tanggal_kadaluarsa']
    search_fields = ['nama', 'tempat_produksi']
    
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile' 
    
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    
admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)

# Register your models here.
