from django import forms
from .models import Founder , Investor, FundingApplication, FundingRequest, Industry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Investor, Founder

# Investor Form
class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'startup_name', 'investment_goal', 'image']

# Founder Form
class FounderForm(forms.ModelForm):
    class Meta:
        model = Founder
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role', 'biography', 'company']

# Funding Form
class FundingApplicationForm(forms.ModelForm):
    class Meta:
        model = FundingApplication
        fields = ['project_name', 'funding_amount', 'description']

# Reguest funbding
class FundingRequestForm(forms.ModelForm):
    class Meta:
        model = FundingRequest
        fields = ['title', 'description', 'amount_requested', 'industry']


class UserRegistrationForm(UserCreationForm):
    # You can add any additional fields if needed, such as email, etc.
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class InvestorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['first_name', 'last_name', 'email', 'startup_name', 'investment_goal']

class FounderRegistrationForm(forms.ModelForm):
    class Meta:
        model = Founder
        fields = ['first_name', 'last_name', 'email', 'company', 'biography']

