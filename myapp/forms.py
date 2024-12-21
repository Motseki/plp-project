from django import forms
from .models import Founder , Investor

class FounderForm(forms.ModelForm):
    class Meta:
        model = Founder
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'biography']


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'startup_name', 'investment_goal', 'image']