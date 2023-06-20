

from django.urls import path

from . import views

from django.contrib.auth import views as auth_views



urlpatterns = [
    
    # HomePage
    path('', views.home, name='home'),

    # Register / Login / Logout
    path('register/', views.register, name='register'),
    path('my-login/', views.my_login, name='my-login'),
    path('user-logout/', views.user_logout, name='user-logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Thought
    path('post-thought', views.post_thought, name="post-thought"),
    path('my-thoughts', views.my_thoughts, name="my-thoughts"),
    path('update-thought/<int:pk>', views.update_thought, name="update-thought"),
    path('delete-thought/<int:pk>', views.delete_thought, name="delete-thought"),

    # Profile management
    path('profile-management', views.profile_management, name="profile-management"),
    path('delete-account', views.delete_account, name="delete-account"),

    # Reset user's password
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="password-reset/password-reset.html"), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password-reset/password-reset-sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset/password-reset-form.html"), name='password_reset_confirm'), 
    # path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset/password-reset-complete.html"), name='password_reset_complete'),

]