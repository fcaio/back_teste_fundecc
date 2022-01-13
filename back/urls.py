"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from processadorArquivos.api import arquivos_router

api_routes = []
api_routes.extend(arquivos_router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Isso faz com que as rotas que iniciadas com api sejam resolvidas
    # com a lista de rotas definidas no app processadorArquivos
    path('api/', include(api_routes)),

]
