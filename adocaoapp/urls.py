from django.contrib import admin
from django.urls import path
from django.urls import path, include # include já estava aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categorias/', include('categories.urls')), # Rota para o app categories com prefixo 'api/'
    path('api/products/', include('apps.products.urls')),
    path('api/socialnetworks/', include('apps.socialnetworks.urls', namespace='socialnetworks')), # Usando api/ e namespace
    path('api/clients/', include('apps.clients.urls', namespace='clients')), # Usando api/ e namespace
    path('api/orders/', include('apps.orders.urls', namespace='orders')), # Usando api/ e namespace
]