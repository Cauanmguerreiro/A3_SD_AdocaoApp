from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialnetworkViewSet
from . import views # Alterado conforme instrução

app_name = 'socialnetworks'

router = DefaultRouter()
router.register(r'', views.SocialnetworkViewSet, basename='socialnetwork') # Mantendo um basename consistente

urlpatterns = [
    path('', include(router.urls)),
]
