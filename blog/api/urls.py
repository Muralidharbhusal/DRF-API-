from django.urls import path
from .views import UserList, UserDetail, PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
	path('users/', UserList.as_view()), 
	path('users/<int:pk>/', UserDetail.as_view()),

	path('', PostList.as_view()),
	path('<int:pk>/', PostDetail.as_view()),


	path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]