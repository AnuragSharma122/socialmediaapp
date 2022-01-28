from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import index, createPosts, register, user_login
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    path("", index),
    path("postcreate/",createPosts),
    path("register/", register),
    path("login/", user_login),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
