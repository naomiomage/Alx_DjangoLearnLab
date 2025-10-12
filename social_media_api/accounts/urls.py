from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserListView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user-list'),
     
     # Follow / Unfollow URLs (must match ALX checker)
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),

    # Followers & Following lists
    path('me/following/', views.following_list, name='following_list'),
    path('me/followers/', views.followers_list, name='followers_list'),
]
