from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from movie.views import MovieViewSet

router = DefaultRouter()
router.register('movie', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
