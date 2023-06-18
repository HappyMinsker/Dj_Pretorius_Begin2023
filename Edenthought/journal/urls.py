

from django.urls import path

from . import views





urlpatterns = [
    
    # HomePage
    path('', views.home, name='home'),

    # Register / Login / Logout
    path('register/', views.register, name='register'),
    path('my-login/', views.my_login, name='my-login'),
    path('user-logout/', views.user_logout, name='user-logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),




]