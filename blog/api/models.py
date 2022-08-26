from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	title = models.CharField(max_length=50)
	body = models.TextField()
	image = models.ImageField(null =True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']