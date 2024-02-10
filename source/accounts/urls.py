from django.urls import path
from .views import UserCreateView, UserLoginView, UserLogoutView, UserProfileView, EditProfileView, UserDetailView
from django.contrib.auth.views import LogoutView
app_name = 'accounts'

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_create'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
