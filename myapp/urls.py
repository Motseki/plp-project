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
]
