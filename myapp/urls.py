from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path('', views.home, name='home'),
	path('investors/', views.investor_list, name='investor_list'),
	path('founders/', views.founder_list, name='founder_list'),
	# Add Views
    path('investors/add/', views.add_investor, name='add_investor'),
    path('founders/add/', views.add_founder, name='add_founder'),
    
    # Edit Views
    path('investors/edit/<int:pk>/', views.edit_investor, name='edit_investor'),
    path('founders/edit/<int:pk>/', views.edit_founder, name='edit_founder'),
    
    # Delete Views
    path('investors/delete/<int:pk>/', views.delete_investor, name='delete_investor'),
    path('founders/delete/<int:pk>/', views.delete_founder, name='delete_founder'),
	


	# path('add_founders/', views.add_founder, name='add_founder'),
	# path('add_investors/', views.add_investor, name='add_investor'),
	path('view_investors/', views.investor_page, name='investor_page'),
	path('view_founders/', views.founders_page, name='founders_page'),

	path('apply-for-funding/', views.apply_for_funding, name='apply_for_funding'),
    path('funding-status/', views.funding_status, name='funding_status'),
	path('application/<int:application_id>/', views.view_application_details, name='view_application_details'),
	path('application/<int:application_id>/approve/', views.approve_application, name='approve_application'),
	path('application/<int:application_id>/reject/', views.reject_application, name='reject_application'),

   	path('available-funding/', views.available_funding_applications, name='available_funding_applications'),
    path('apply-for-funding/<int:application_id>/', views.apply_for_funding, name='apply_for_funding'),

	path('funding-opportunities/', views.ListFundingOpportunitiesView.as_view(), name='list_funding_opportunities'),
	#path('funding-opportunities/', views.list_funding_opportunities, name='funding_opportunities'),
    path('toggle-interest/<int:opportunity_id>/', views.toggle_funding_interest, name='toggle_funding_interest'),

	path('fundingopportunities/', views.list_funding_opportunities, name='funding_opportunities'),
    path('sponsored_projects/', views.sponsored_projects, name='sponsored_projects'),
    path('toggle_funding_interest/<int:opportunity_id>/', views.toggle_funding_interest, name='toggle_funding_interest'),

	path('add_funding_request/', views.add_funding_request, name='add_funding_request'),
    path('funding_request_success/', views.funding_request_success, name='funding_request_success'),
	#  path('apply-for-funding/<int:application_id>/', views.apply_for_funding, name='apply_for_funding'),

	path('register/investor/', views.register_investor, name='register_investor'),
    path('register/founder/', views.register_founder, name='register_founder'),

	path('funding_connect/', views.index, name='index'),
	path('view_resources', views.index_resouces, name='index_resources'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('resource/<int:resource_id>/', views.resource_detail, name='resource_detail'),
	path('view_group/', views.home_screen, name='home_screen'),
    # path("login", views.IndexView.as_view(), name="index"), 
	path('dashboard/', views.dashboard, name='dashboard'),
	path('register/', views.register, name='register'),  
	path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
	# path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('logout/', views.custom_logout, name='logout'),
	path('profile/', views.profile, name='profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	# path('user-management/', views.user_management, name='user_management'),
	# path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
	path('user-management/', views.user_management, name='user_management'),
    path('user/add/', views.add_user, name='add_user'),
    path('user/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('user/disable/<int:user_id>/', views.disable_user, name='disable_user'),
    path('user/suspend/<int:user_id>/', views.suspend_user, name='suspend_user'),
]
