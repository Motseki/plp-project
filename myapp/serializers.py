from rest_framework import serializers
from .models import Investor, Founder

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'investment_amount', 'date_joined']

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'biography', 'company', 'date_joined']