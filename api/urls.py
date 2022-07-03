from django.urls import path
from . import views

app_name = "proverb"

urlpatterns = [
    path("create/", views.ProverbCreateAPI.as_view(), name="api_create"),
    path("update/<int:pk>", views.ProverbUpdateAPI.as_view(), name="api_update"),
    path("delete/<int:pk>", views.ProverbDeleteAPI.as_view(), name="api_delete"),
    path("", views.ProverbListAPI.as_view(), name="api_list"),
]


# from rest_framework.routers import DefaultRouter
# from api.views import ProverbViewSet


# router = DefaultRouter()
# router.register(r'proverbs', ProverbViewSet, basename = 'proverbs')


# urlpatterns =[

# ] + router.urls

# # 127.0.0.1:8000/api/proverbs/
