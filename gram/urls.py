from django.conf.urls import url, include
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    url(r'^$', PostListView.as_view(), name='index'),
    url(r'user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    url(r'post/new',PostCreateView.as_view(), name='post-create'),
    url(r'^image/$', views.add_image, name='upload_image'),
    url(r'^ search/',views.search, name='search'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
    url(r'^follow/(?P<user_id>\d+)', views.follow, name='follow'),
    url(r'post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'post/<int:pk>/update',PostUpdateView.as_view(), name = 'post-update'),
    url(r'post/<int:pk>/delete',PostDeleteView.as_view(), name = 'post-delete'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  