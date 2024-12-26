from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Import settings
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_investor = models.BooleanField(default=False)
    is_founder = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Investor model
class Investor(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="investor")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    startup_name = models.CharField(max_length=200)
    investment_goal = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='investor_images/', blank=True, null=True)
    funding_applications = models.ManyToManyField(
        'FundingApplication', related_name="interested_in_investors", blank=True
    )
    funding_opportunities = models.ManyToManyField(
        'FundingRequest', related_name="interested_investors_set", blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.startup_name}"
    
# Industry model (make sure this is defined before it's used in FundingRequest)
class Industry(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class FundingRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    interested_investors = models.ManyToManyField(
        'Investor', related_name='funding_opportunities_set', blank=True  # updated related_name
    )

    def __str__(self):
        return self.title


# Founder model
class Founder(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="founder")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ResourceCategory model
class ResourceCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name


# Resource model
class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resource_files/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# UserProfile model
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    avatar_url = models.URLField()

    def __str__(self):
        return self.name


# Group model
class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# FundingApplication model
class FundingApplication(models.Model):
    founder = models.ForeignKey(Founder, on_delete=models.CASCADE, related_name='funding_applications')
    project_name = models.CharField(max_length=255)
    funding_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )

    def __str__(self):
        return f"{self.project_name} - {self.founder.first_name} {self.founder.last_name}"
    

class FundingOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
