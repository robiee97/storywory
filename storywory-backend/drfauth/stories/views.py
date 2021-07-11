from .serializers import PostSerializer
from .models import Post
from rest_framework import  generics, permissions
from .permissions import  IsOwner
from rest_framework.response import Response
from rest_framework import status
from .producer import produceData
import requests

# Create your views here.
class PostViewSet(generics.GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated)
        
    def post(self,request):
        serializer= self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        #event produced to kafka
        produceData('Addpost',serializer.data)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    
#open API
class LikePostView(generics.GenericAPIView):   
    
    def post(self, request,post_id):
        post = Post.objects.get(pk=post_id)
        user = self.request.user
        
        if user.is_authenticated:
            if user in post.likes.all():
                like = False
                post.likes.remove(user)
                #dislike api call
                requests.post('http://localhost:8080/post/dislike/'+post_id)
                return Response(like)
            else:
                like = True
                post.likes.add(user)
                #like api call
                requests.post('http://localhost:8080/post/like/'+post_id)
                return Response(like)
        return Response('Not authenticated',status=status.HTTP_400_BAD_REQUEST)