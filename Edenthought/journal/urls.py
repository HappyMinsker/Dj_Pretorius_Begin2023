from django.urls import path

from .views import register, home, tasks, create_task, update_task, delete_task, success, my_login, dashboard, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', tasks, name='tasks'),
    path('create-task/', create_task, name ='create-task'),
    path('update-task/<int:pk>', update_task, name ='update-task'),
    path('delete-task/<int:pk>', delete_task, name ='delete-task'),

    path('register/', register, name='register'),
    path('success/',success, name='success'),

    path('my-login/',my_login, name='my-login'),
    path('dashboard/',dashboard, name='dashboard'),
    path('user-logout/',user_logout, name='user-logout'),

]