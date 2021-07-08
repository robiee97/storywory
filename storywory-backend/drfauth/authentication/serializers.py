from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User
from django.contrib import auth

from stories.models import Post

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email', 'username', 'fullname', 'password', ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        fullname=attrs.get('fullname','')
        
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(max_length=255,min_length=3)
    password= serializers.CharField(max_length=68,min_length=6, write_only=True)
    username= serializers.CharField(max_length=255,min_length=3,read_only=True)
    tokens= serializers.CharField(max_length=68,min_length=6,read_only=True)
    
    class Meta:
        model=User
        fields=['email','password','username','tokens']

    def validate(self, attrs):
        email= attrs.get('email','')
        password= attrs.get('password','')

        user= auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials, Try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('User needs to verify account')
        
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens(),
        }

class LogoutSerializer(serializers.Serializer):
    refresh= serializers.CharField()

    default_error_messages={
        'bad_token': ('token is expired or invalid')
    }

    def validate(self, attrs):
        self.token=attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'fullname', 'bio', 'profile_pic']
        
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.save()
        return user


class UserPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','photo', 'text', 'location', 'number_of_likes', 'posted_on')

class UserProfileSerializer(serializers.ModelSerializer):
    user_posts = serializers.SerializerMethodField('populatepost')
    class Meta:
        model = User
        fields = ('username', 'fullname', 'bio', 'profile_pic', 'user_posts')

    def populatepost(self, obj):
        serializer = UserPostsSerializer(Post.objects.filter(owner=obj), many=True)
        return serializer.data
