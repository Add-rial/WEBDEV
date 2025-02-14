from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms

from .models import Passenger

class AdminPassenger(admin.ModelAdmin):
    list_display = ('name', 'booked_by', 'bus')
    search_fields = ('name', 'booked_by', 'bus')


class CustomUserChangeForm(forms.ModelForm):
    wallet = forms.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = User
        fields = '__all__'

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'wallet', 'is_staff', 'is_superuser')

    def wallet(self, obj):
        return obj.wallet_balance
    wallet.admin_order_field = 'wallet'
    wallet.short_description = "Wallet"
    fieldsets = UserAdmin.fieldsets + (
        ("Wallet Information", {"fields": ("wallet",)}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Passenger, AdminPassenger)
