from django.urls import path
from .views import signup_user, login_user, logout_user, user_profile, change_password

app_name = 'users'

urlpatterns = [
     path('signup/', signup_user, name='signup'),
     path('login/', login_user, name='login'),
     path('logout/', logout_user, name='logout'),
     path('profile/', user_profile, name='user_profile'),
     path('password/', change_password, name='change_password'),
     
]    