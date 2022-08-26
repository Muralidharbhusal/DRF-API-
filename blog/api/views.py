from django.contrib.auth import get_user_model 
from rest_framework import generics
from .models import Post, Comment
from .permissions import *
from .serializers import *


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


	'''def get_comments(self, post):

		data = Comment.objects.filter(post=post).values('user_id', 'user__username', 'comment')
		return data'''



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): 
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer



class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


   