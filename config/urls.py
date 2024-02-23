"""
URL configuration for config project.

The `urlpatterns` list routes URLs to apiviews. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function apiviews
    1. Add an import:  from my_app import apiviews
    2. Add a URL to urlpatterns:  path('', apiviews.home, name='home')
Class-based apiviews
    1. Add an import:  from other_app.apiviews import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studies.urls', namespace='studies')),
    path('users/', include('users.urls', namespace='users')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('subscription/', include('subscription.urls', namespace='subscription')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
