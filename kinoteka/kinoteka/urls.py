"""
URL configuration for kinoteka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import routers
from films.views import *

router = routers.SimpleRouter()
router.register(r"films", FilmViewSet)
router.register(r"type", TypeViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # path('api/v1/filmcards/', FilmsAPIView.as_view()),
    # path('api/v1/filmcard/<int:pk>/', FilmAPIView.as_view())
    path('', include('main.urls'))
]
