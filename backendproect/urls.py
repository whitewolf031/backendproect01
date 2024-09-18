"""
URL configuration for backendproect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from proect.views import *

# router = routers.SimpleRouter()
# router.register(r'startproject', ProectCRUD, basename='project')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),
    #Cookie
    path('drf-auth/', include('rest_framework.urls')), #SessionAuthentication

    path('person-list-post/', ProectlistCreate.as_view()),
    # path('personlist/', Proectlist.as_view()),
    # path('personcreate/', ProectCreate.as_view()),
    path('person-update/<int:pk>/', ProectUpdate.as_view()),
    path('person-get-del/<int:pk>/', ProectDestroy.as_view()),

    #Djoser
    path('api/v1/auth/', include('djoser.urls')),  # Authentication Djoser Registeratsiya
    re_path(r'^auth/', include('djoser.urls.authtoken')), #Autorizasiya

    #JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('person-list/', ProectCRUD.as_view({"get": "list"})),
    # path('person-create/', ProectCRUD.as_view({"post": "create"})),
    # path('person-get_id/<int:pk>/', ProectCRUD.as_view({"get": "retrieve"})),
    # path('person-put/<int:pk>/', ProectCRUD.as_view({"put": "update"})),
    # path('person-patch/<int:pk>/', ProectCRUD.as_view({"patch": "partial_update"})),
    # path('person-del/<int:pk>/', ProectCRUD.as_view({"delete": "destroy"})),
]
