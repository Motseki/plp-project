from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path('', views.home, name='home'),
	path('investors/', views.investor_list, name='investor_list'),
	path('founders/', views.founder_list, name='founder_list'),
	path('add_founders/', views.add_founder, name='add_founder'),
	path('add_investors/', views.add_investor, name='add_investor'),
	path('view_investors/', views.investor_page, name='investor_page'),
	path('view_founders/', views.founders_page, name='founders_page'),
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
