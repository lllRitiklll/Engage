from django.urls import path
from .views import signup, profile, logout_user, edit_profile, follow_toggle, search_users ,notifications_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/<str:username>/', profile, name='profile'),
    path('logout/', logout_user, name='custom_logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('follow/<str:username>/', follow_toggle, name='follow_toggle'),
    path('search/', search_users, name='search_users'),
    path('notifications/', notifications_view, name='notifications'),
    
]