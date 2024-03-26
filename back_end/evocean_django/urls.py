"""
URL configuration for evocean_django project.

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
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django_firebase_auth import urls as firebase_urls

from evocean_django.settings import INSTALLED_APPS

schema_view = get_schema_view(
    openapi.Info(
        title="EVOCEAN API",
        default_version="v1",
        description="EVOCEAN Project API list",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="socrat.nguyenanhbinh@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def auto_router(router):
    for app in INSTALLED_APPS:
        try:
            app_router = __import__(f"{app}.urls", fromlist=["router"]).router
            router.registry.extend(app_router.registry)
            print(f"Auto register {app} router")
        except ImportError:
            pass
        except AttributeError:
            pass

    return router


router = routers.DefaultRouter()
# router.register(r"users", UserViewSet)
router = auto_router(router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-auth-firebase/", include(firebase_urls)),
    path("api-auth/logout/", LogoutView.as_view(), name="logout"),  # added line
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
