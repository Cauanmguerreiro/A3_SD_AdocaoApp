from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'', CategoryViewSet, basename='category') # r'' para a raiz do app

urlpatterns = [
    path('', include(router.urls)),
]
