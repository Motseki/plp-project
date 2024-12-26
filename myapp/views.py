from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets
#from django.contrib.auth.models import User

from .models import Group, FundingApplication, Industry, Investor, Founder, FundingRequest, ResourceCategory, Resource, UserProfile
from  .forms import FounderForm, InvestorForm, FundingApplicationForm, FundingRequestForm
from .models import FundingApplication, FundingRequest

from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Investor, Founder

# from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, InvestorRegistrationForm, FounderRegistrationForm
from django.contrib.auth import login

# from django.shortcuts import render
from django.views.generic import ListView
from .models import FundingOpportunity

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required

# from django.shortcuts import get_object_or_404, redirect
# from .models import FundingApplication, Invest

from django.http import HttpResponse
from django.contrib.auth import logout

from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

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

@login_required
def dashboard(request):
    user = request.user

    # Fetch funding applications based on user role
    if user.is_staff:  # Admin view
        applications = FundingApplication.objects.all()
    else:  # Regular user (founder) view
        applications = FundingApplication.objects.filter(founder__user=user)

    # Fetch all founders to display
    founders = Founder.objects.all()

    context = {
        'user': user,
        'applications': applications,
        'founders': founders,  # Add founders to the context
    }
    return render(request, 'dashboard.html', context)



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
#         return redirect('myapp:dashboard')  # Restrict to admins

#     users = User.objects.all()
#     return render(request, 'profile/user_management.html', {'users': users})

@login_required
def user_management(request):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')  # Restrict to admins

    # Use get_user_model to get the custom user model
    users = get_user_model().objects.all()
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

def investor_list(request):
    investors = Investor.objects.all()  # Get all investors from the database
    
    # Check if the request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Return only the list of investors as HTML when it's an AJAX request
        return render(request, 'dashboard/investor_list_partial.html', {'investors': investors})
    
    # Otherwise, return the full page with the investors' data
    return render(request, 'dashboard//investor_list.html', {'investors': investors})

def founder_list(request):
    founders = Founder.objects.all()  # Get all founders from the database
    
    # Check if the request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Return only the list of founders as HTML when it's an AJAX request
        return render(request, 'dashboard//founder_list_partial.html', {'founders': founders})
    
    # Otherwise, return the full page with the founders' data
    return render(request, 'dashboard//founder_list.html', {'founders': founders})


# Add Investor
def add_investor(request):
    if request.method == "POST":
        form = InvestorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:investor_list')
    else:
        form = InvestorForm()
    return render(request, 'dashboard//add_investor.html', {'form': form})

# Add Founder
def add_founder(request):
    if request.method == "POST":
        form = FounderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:founder_list')
    else:
        form = FounderForm()
    return render(request, 'dashboard//add_founder.html', {'form': form})

# Edit Investor
def edit_investor(request, pk):
    investor = get_object_or_404(Investor, pk=pk)
    if request.method == "POST":
        form = InvestorForm(request.POST, request.FILES, instance=investor)
        if form.is_valid():
            form.save()
            return redirect('myapp:investor_list')
    else:
        form = InvestorForm(instance=investor)
    return render(request, 'dashboard//edit_investor.html', {'form': form})

# Edit Founder
def edit_founder(request, pk):
    founder = get_object_or_404(Founder, pk=pk)
    if request.method == "POST":
        form = FounderForm(request.POST, instance=founder)
        if form.is_valid():
            form.save()
            return redirect('myapp:founder_list')
    else:
        form = FounderForm(instance=founder)
    return render(request, 'dashboard//edit_founder.html', {'form': form})

# Delete Investor
def delete_investor(request, pk):
    investor = get_object_or_404(Investor, pk=pk)
    if request.method == "POST":
        investor.delete()
        return redirect('myapp:investor_list')
    return render(request, 'dashboard//delete_investor.html', {'investor': investor})

# Delete Founder
def delete_founder(request, pk):
    founder = get_object_or_404(Founder, pk=pk)
    if request.method == "POST":
        founder.delete()
        return redirect('myapp:founder_list')
    return render(request, 'dashboard//delete_founder.html', {'founder': founder})

# Apply for funding
@login_required
def apply_for_funding(request):
    if request.method == 'POST':
        form = FundingApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.founder = request.user
            application.save()
            return redirect('myapp:funding_status')  # Redirect to a page showing funding status
    else:
        form = FundingApplicationForm()
    return render(request, 'dashboard/apply_for_funding.html', {'form': form})


@login_required
def funding_status(request):
    applications = request.user.funding_applications.all()
    return render(request, 'dashboard/funding_status.html', {'applications': applications})

def view_application_details(request, application_id):
    application = get_object_or_404(FundingApplication, id=application_id)
    return render(request, 'dashboard/view_application_details.html', {'application': application})

@login_required
def approve_application(request, application_id):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')

    application = get_object_or_404(FundingApplication, id=application_id)
    application.status = 'Approved'
    application.save()
    return redirect('myapp:dashboard')

@login_required
def reject_application(request, application_id):
    if not request.user.is_staff:
        return redirect('myapp:dashboard')

    application = get_object_or_404(FundingApplication, id=application_id)
    application.status = 'Rejected'
    application.save()
    return redirect('myapp:dashboard')


@login_required
def available_funding_applications(request):
    applications = FundingApplication.objects.all()  # Get all funding applications
    return render(request, 'investors/available_funding_applications.html', {'applications': applications})

@login_required
def list_funding_opportunities(request):
    investor = request.user.investor  # Assuming logged-in user is an investor
    opportunities = FundingRequest.objects.exclude(interested_investors=investor)  # Get funding opportunities not already sponsored by this investor
    return render(request, 'investors/funding_opportunities.html', {'opportunities': opportunities})


@login_required
def toggle_funding_interest(request, opportunity_id):
    try:
        # Ensure the user has an associated Investor profile
        if not hasattr(request.user, 'investor'):
            return HttpResponse("You must be an investor to perform this action.", status=403)

        investor = request.user.investor
        opportunity = get_object_or_404(FundingRequest, id=opportunity_id)

        # Toggle sponsorship
        if opportunity in investor.sponsored_projects.all():
            investor.sponsored_projects.remove(opportunity)
        else:
            investor.sponsored_projects.add(opportunity)

        return redirect('investors:funding_opportunities')

    except Exception as e:
        # Log the error for debugging
        print(f"Error in toggle_funding_interest: {e}")
        return HttpResponse(f"An error occurred: {e}", status=500)




class ListFundingOpportunitiesView(ListView):
    model = FundingOpportunity  # Ensure this is the correct model
    template_name = 'funding_opportunities_list.html'  # Ensure this matches the template name
    context_object_name = 'opportunities'

@login_required
def sponsored_projects(request):
    investor = request.user.investor
    sponsored_projects = investor.sponsored_projects.all()  # Get all sponsored projects for the logged-in investor

    return render(request, 'investors/sponsored_projects.html', {'sponsored_projects': sponsored_projects})


@login_required
def add_funding_request(request):
    if request.method == 'POST':
        form = FundingRequestForm(request.POST)
        if form.is_valid():
            funding_request = form.save(commit=False)
            funding_request.founder = request.user.founder  # Associate with the logged-in founder
            funding_request.save()
            return redirect('funding_request_success')
    else:
        form = FundingRequestForm()

    return render(request, 'add_funding_request.html', {'form': form})

@login_required
def funding_request_success(request):
    return render(request, 'funding_request_success.html')


def register_investor(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        investor_form = InvestorRegistrationForm(request.POST)
        
        if user_form.is_valid() and investor_form.is_valid():
            # Save user and investor information
            user = user_form.save()
            investor = investor_form.save(commit=False)
            investor.user = user
            investor.save()
            
            login(request, user)  # Automatically log the user in
            return redirect('home')  # Redirect to the home page or dashboard
            
    else:
        user_form = UserRegistrationForm()
        investor_form = InvestorRegistrationForm()
    
    return render(request, 'register_investor.html', {
        'user_form': user_form,
        'investor_form': investor_form
    })

def register_founder(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        founder_form = FounderRegistrationForm(request.POST)
        
        if user_form.is_valid() and founder_form.is_valid():
            # Save user and founder information
            user = user_form.save()
            founder = founder_form.save(commit=False)
            founder.user = user
            founder.save()
            
            login(request, user)  # Automatically log the user in
            return redirect('home')  # Redirect to the home page or dashboard
            
    else:
        user_form = UserRegistrationForm()
        founder_form = FounderRegistrationForm()
    
    return render(request, 'register_founder.html', {
        'user_form': user_form,
        'founder_form': founder_form
    })

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # If the user is an investor, create an investor profile
        if instance.is_investor:  # You could use a flag or another method to identify role
            Investor.objects.create(user=instance)
        elif instance.is_founder:  # Or if the user is a founder
            Founder.objects.create(user=instance)


