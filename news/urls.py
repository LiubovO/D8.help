from django.urls import path
from .views import PostsList, PostsDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostsList.as_view(), name='postlist'),
    path('<int:pk>', PostsDetail.as_view(), name='post'),
    path('news/<int:pk>', PostsDetail.as_view(), name='post'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),

]
