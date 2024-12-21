from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path('', views.home, name='home'),
	path('investors/', views.investor_list, name='investor_list'),
	path('founders/', views.founder_list, name='founder_list'),
	path('add_founders/', views.add_founder, name='add_founder'),
	 path('add_investors/', views.add_investor, name='add_investor'),
    # path("login", views.IndexView.as_view(), name="index"),
]
