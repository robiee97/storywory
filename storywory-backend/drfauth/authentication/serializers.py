from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from django.contrib import auth


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

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
        return super().validate(attrs)