from django.contrib import admin
from .models import Investor, Founder, FundingOpportunity, FundingRequest, FundingApplication, Industry
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_investor', 'is_founder')
    list_filter = ('is_staff', 'is_investor', 'is_founder', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    # Add additional fields for display in the user edit form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('is_investor', 'is_founder')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_investor', 'is_founder'),
        }),
    )

# Register the CustomUser model with the customized UserAdmin
admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'startup_name', 'investment_goal')
    search_fields = ('first_name', 'last_name', 'startup_name')

@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company')
    search_fields = ('first_name', 'last_name', 'company')

@admin.register(FundingOpportunity)
class FundingOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount_requested')
    search_fields = ('title',)

@admin.register(FundingRequest)
class FundingRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount_requested')  # Use the method to get the founder's name
    search_fields = ('title', 'founder__first_name')

    def founder_name(self, obj):
        funding_application = FundingApplication.objects.filter(funding_request=obj).first()
        return funding_application.founder.first_name if funding_application else None

    founder_name.short_description = 'Founder'

@admin.register(FundingApplication)
class FundingApplicationAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'funding_amount', 'status', 'founder')
    search_fields = ('project_name', 'founder__first_name')

# Register Industry model
@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the 'name' field in the list view
    search_fields = ('name',)  # Enable search by 'name'

