from django.urls import path
from .views import EditProfileView, GetProfileView, LoginApiView, LogoutApiView, RegisterView, VerifyEmail

from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('logout/', LogoutApiView.as_view(), name='logout'),   
    

    path('profile/<str:username>', GetProfileView.as_view(), name="getprofile"),
    path('myprofile/', EditProfileView.as_view(), name="myprofile"),

]
