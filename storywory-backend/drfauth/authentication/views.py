from logging import raiseExceptions
from rest_framework import generics, status, views
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, UserInfoSerializer, UserProfileSerializer, LogoutSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from rest_framework import permissions


class RegisterView(generics.GenericAPIView):

    serializer_class= RegisterSerializer
    
    def post(self,request):
        userformdata = request.data
        serializer= self.serializer_class(data=userformdata)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site= get_current_site(request).domain
        relativeLink=reverse('email-verify')
        absurl="http://"+current_site+relativeLink+"?token="+str(token)
        
        email_body='Hi '+user.fullname+" please verify your email using below link \n" + absurl
        data={'email_body':email_body, 'to_email':user.email, 'email_subject':'verify your Email'}

        Util.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    serializer_class= EmailVerificationSerializer
    
    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(generics.GenericAPIView):

    serializer_class= LoginSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutApiView(generics.GenericAPIView):
    serializer_class= LogoutSerializer
    permission_classes =(permissions.IsAuthenticated,)

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EditProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer
    permission_classes =(permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


#open to all API
class GetProfileView(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny,)