from django.contrib.auth import get_user_model 
from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	comments = serializers.SerializerMethodField()
	
	class Meta:
		fields = ('id', 'owner', 'title', 'body', 'image', 'created_at','comments')
		model = Post

	def get_comments(self, post):

		data = Comment.objects.filter(post=post).values('id', 'comment', 'owner__username')
		return data




class UserSerializer(serializers.ModelSerializer): # new
	class Meta:
		model = get_user_model()
		fields = ('id', 'username',)


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'owner']

    