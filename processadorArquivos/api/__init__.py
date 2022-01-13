from rest_framework import routers

from .viewsets import ArquivoViewSet

# Registrar a rota arquivo e linka-la com a view ArquivoViewSet

arquivos_router = routers.DefaultRouter()

arquivos_router.register(r'arquivo', ArquivoViewSet, basename='Arquivo')
