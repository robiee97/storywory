from django.urls import path
from .views import EditProfileView, GetProfileView, LoginApiView, RegisterView, VerifyEmail

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    
    path('profile/<str:username>', GetProfileView.as_view(), name="getprofile"),
    path('myprofile/', EditProfileView.as_view(), name="myprofile"),

]
