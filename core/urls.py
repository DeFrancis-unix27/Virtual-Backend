from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import TestimonialsAPI

testimonial_list = TestimonialsAPI.as_view({
    'get': 'list',
    'post': 'create'
})
testimonial_detail = TestimonialsAPI.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path("", views.root_view),
    path("api/home/", views.HomeAPI.as_view(), name="home"),
    path("api/about/", views.AboutAPI.as_view(), name="about"),
    path("api/services/", views.ServicesAPI.as_view(), name="services"),
    path("api/testimonials/", testimonial_list, name="testimonials-list"),
    path("api/testimonials/<int:pk>/", testimonial_detail, name="testimonials-detail"),
    path("api/gallery/", views.GalleryListAPI.as_view(), name="gallery-list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)