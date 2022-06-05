from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('todo/<int:pk>/', PostDetail.as_view()),
    path('todo/', PostList.as_view()),
]
