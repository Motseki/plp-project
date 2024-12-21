from django.contrib import admin
from .models import Founder, Investor


# Register your models here.
@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'company', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'role')
    list_filter = ('date_joined',)

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'investment_goal', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date_joined',)
