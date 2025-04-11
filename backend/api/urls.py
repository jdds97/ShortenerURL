from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import URLShortenerView

router = DefaultRouter()
router.register(r'shorten', URLShortenerView, basename='shorten')

urlpatterns = [
    path('', include(router.urls)),
]
