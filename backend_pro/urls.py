"""
URL configuration for backend_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.generic import RedirectView

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url="/static/favicon.ico")),
    path("", include("core.urls")),
    path("api/blog/", include("django_apps.blog.urls")),
    path("api/contact/", include("django_apps.contact.urls")),
    path("api/projects/", include("django_apps.projects.urls")),
    path("api/csrf/", get_csrf_token, name="csrf_token"),
    # Clean URL endpoints
    path("blogs/", include("django_apps.blog.urls")),
    path("contact/", include("django_apps.contact.urls")),
    path("projects/", include("django_apps.projects.urls")),
    path("dashboard/", include("django_apps.dashboard.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
