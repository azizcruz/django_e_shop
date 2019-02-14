from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    '''
        Custom View For Custom User Admin
    '''
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'country', 'active']
    filter_display = ['active']
    fieldsets = [
        ['Personal info',
        {
            'fields': [
                'username',
                'password',
                'first_name',
                'last_name',
                'country',
                'address',
                'date_joined',
                'groups',
                'active'   
            ]
        }
        ]
    ]

admin.site.register(CustomUser, CustomUserAdmin)