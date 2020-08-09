from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url('account/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  