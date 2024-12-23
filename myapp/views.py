from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets
from django.contrib.auth.models import User

from .models import Group, Industry, Investor, Founder, FundingRequest, ResourceCategory, Resource, UserProfile
from  .forms import FounderForm, InvestorForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from django.http import HttpResponse
from django.contrib.auth import logout

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.decorators import login_required

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# Use login_required to ensure only authenticated users can access this view
@login_required
def dashboard(request):
    # Fetch any user-specific data if needed
    user = request.user  # Get the currently logged-in user
    context = {
        'user': user,
    }
    return render(request, 'dashboard.html', context)


# def profile(request):
#     return render(request, 'myapp/profile.html')

def profile(request):
    # Assuming you have a User profile model or additional user info
    user = request.user
    return render(request, 'profile/profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('myapp:profile')  # Redirect to the profile page after saving
    else:
        form = UserChangeForm(instance=request.user)

    # Add CSS classes to form fields
    form.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    form.fields['last_name'].widget.attrs.update({'class': 'form-control'})
    form.fields['email'].widget.attrs.update({'class': 'form-control'})
    form.fields['password'].widget.attrs.update({'class': 'form-control'})

    return render(request, 'profile/edit_profile.html', {'form': form})

def logout_view(request):
    print("Logging out...")
    logout(request)
    return redirect('myapp:home')  # or wherever you'd like to redirect after logout

def custom_logout(request):
    logout(request)
    return redirect('myapp:home')  # Redirect to the home page after logout

# @login_required
# def user_management(request):
#     if not request.user.is_staff:
#         return redirect('dashboard')  # Redirect non-admin users to the dashboard
    
#     users = User.objects.all()
#     return render(request, 'profile/user_management.html', {'users': users})

# @login_required
# def delete_user(request, user_id):
#     if not request.user.is_staff:
#         return redirect('dashboard')  # Restrict deletion to admin users
    
#     user = get_object_or_404(User, id=user_id)
#     user.delete()
#     return redirect('myapp:user_management')

@login_required
def user_management(request):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')  # Restrict to admins

    users = User.objects.all()
    return render(request, 'profile/user_management.html', {'users': users})

@login_required
def add_user(request):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:user_management')
    else:
        form = UserCreationForm()
    return render(request, 'profile/add_user.html', {'form': form})

@login_required
def edit_user(request, user_id):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.is_staff = 'is_staff' in request.POST
        user.save()
        return redirect('myapp:user_management')
    return render(request, 'profile/edit_user.html', {'user': user})

@login_required
def delete_user(request, user_id):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')

    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('myapp:user_management')

@login_required
def disable_user(request, user_id):
    if not request.user.is_staff:
        return redirect('dashboard')

    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    return redirect('myapp:user_management')


@login_required
def suspend_user(request, user_id):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')

    # Example implementation: Suspend by setting a custom field or flag
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    return redirect('myapp:user_management')

