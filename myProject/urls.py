"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path("sers/", include("sers.urls")),
    path("model_serializer/", include("model_serializer.urls")),
    path("school/", include("school.urls")),
    path("req/", include("req.urls")),
    path("demo/", include("view.urls")),
    path("generic/", include("generic.urls")),
    path("mixin/", include("mixin.urls")),
    path("mixin-generic/", include("mixin_generic.urls")),
    path("viewset/", include("viewset.urls")),
    path("generic-viewset/", include("generic_viewset.urls")),
    path("mixin-generic-viewset/", include("mixin_generic_viewset.urls")),
    path("mixin-generic-viewset-router/", include("mixin_generic_viewset_router.urls")),
]
