from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets

from .models import Investor, Founder
from  .forms import FounderForm, InvestorForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def investor_list(request):
    investors = Investor.objects.all()  # Fetch all investors from the database
    return render(request, 'investors/investor_list.html', {'investors': investors})

def founder_list(request):
    # Fetch all founders from the database
    founders = Founder.objects.all()
    # Render the list in a template
    return render(request, 'founders/founders_list.html', {'founders': founders})

def add_founder(request):
    if request.method == 'POST':
        form = FounderForm(request.POST, request.FILES)  # Use request.FILES to handle image uploads
        if form.is_valid():
            form.save()
            return redirect('founder_list')  # Redirect to the list of founders after submission
    else:
        form = FounderForm()

    return render(request, 'founders/add_founder.html', {'form': form})


def add_investor(request):
    if request.method == 'POST':
        form = InvestorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('investor_list')  # Redirect to the list of investors after successful submission
    else:
        form = InvestorForm()

    return render(request, 'investors/add_investor.html', {'form': form})