from django.db import models

class Investor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    startup_name = models.CharField(max_length=200)
    investment_goal = models.DecimalField(max_digits=10, decimal_places=2)  # This field should exist
    date_joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='investor_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.startup_name}"
    
class Founder(models.Model):
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
    
class FundingRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other relevant fields like industry, stage, etc.
    founder = models.ForeignKey(Founder, on_delete=models.CASCADE, related_name='funding_requests') 

class ResourceCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/', blank=True, null=True) 

    def __str__(self):
        return self.name

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resource_files/', blank=True, null=True)
    link = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    # ... fields for user profile information ...
    name = models.CharField(max_length=255)
    avatar_url = models.URLField()

class Group(models.Model):
    # ... fields for group information ...
    name = models.CharField(max_length=255)

class Industry(models.Model):
    # ... fields for industry information ...
    name = models.CharField(max_length=255)