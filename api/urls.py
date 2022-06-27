from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from api.views import ProverbViewSet


router = DefaultRouter()
router.register(r'proverbs', ProverbViewSet, basename = 'proverbs')


urlpatterns =[] + router.urls

# 127.0.0.1:8000/api/proverbs/