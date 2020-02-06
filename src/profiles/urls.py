from django.urls import path
from .views import user_profile_name, hello_world

app_name = 'profiles'

urlpatterns = [
    path('user-profile-name', user_profile_name, name='user-profile-name'),
    path('hello-world', hello_world, name='hello-world'),
]
