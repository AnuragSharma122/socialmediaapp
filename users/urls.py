from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from .views import register
admin.autodiscover()

urlpatterns = [
    # path("register/", register)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
