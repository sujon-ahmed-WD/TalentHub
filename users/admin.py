from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    model = User

    # Admin list view
    list_display = ( 'email', 'first_name', 'last_name', 'role','is_active')
    list_filter = ('is_staff', 'is_active')

    # User detail view
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'role', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # User creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','role', 'password2', 'is_staff', 'is_active')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
