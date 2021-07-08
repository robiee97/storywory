from .models import Post
from rest_framework import serializers
from authentication.models import User

class OwnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'profile_pic')

class PostSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    photo = serializers.CharField(max_length=50)
    
    class Meta:
        model = Post
        fields = ('id', 'owner', 'photo',
                  'text', 'location', 'posted_on',
                  'number_of_likes', )