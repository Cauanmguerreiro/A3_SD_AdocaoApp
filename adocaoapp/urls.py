from django.contrib import admin
from django.urls import path
from django.urls import path, include # Adicionado include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categorias/', include('categories.urls')), # Rota para o app categories com prefixo 'api/'
   path('api/products/', include('apps.products.urls')),
]