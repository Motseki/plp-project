from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets

from .models import Group, Industry, Investor, Founder, FundingRequest, ResourceCategory, Resource, UserProfile
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

def investor_page(request):
    investors = Investor.objects.all().order_by('-date_joined')  # Newest investors first
    return render(request, 'investors/investor_page.html', {'investors': investors})

def founders_page(request):
    founders = Founder.objects.all().order_by('-date_joined')  # Order by newest
    return render(request, 'founders/founders_page.html', {'founders': founders})

def index(request):
    featured_investor = Investor.objects.order_by('?').first()  # Get a random featured investor
    funding_requests = FundingRequest.objects.all()[:3]  # Get the latest 3 funding requests
    return render(request, 'funding_connect/index.html', {
        'featured_investor': featured_investor,
        'funding_requests': funding_requests,
    })

def index_resouces(request):
    resource_categories = ResourceCategory.objects.all()
    return render(request, 'resources/index.html', {
        'resource_categories': resource_categories,
    })

def category_detail(request, category_id):
    category = get_object_or_404(ResourceCategory, pk=category_id)
    resources = category.resource_set.all()  # Get resources for the specific category
    return render(request, 'resources/category_detail.html', {
        'category': category,
        'resources': resources,
    })

def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    return render(request, 'resources/resource_detail.html', {
        'resource': resource,
    })


def home_screen(request):
    # Get sample user profile (replace with actual user profile logic)
    user_profile = UserProfile(name='John Doe', avatar_url='https://example.com/avatar.jpg')

    # Get sample groups (replace with actual group retrieval logic)
    groups = [Group(name='Group 1'), Group(name='Group 2')]

    # Get sample industries (replace with actual industry retrieval logic)
    industries = [Industry(name='Tech'), Industry(name='Finance'), Industry(name='Healthcare')]

    context = {
        'user_profile': user_profile,
        'groups': groups,
        'industries': industries,
    }
    return render(request, 'group/index.html', context)