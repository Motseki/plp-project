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