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
    path("home/", views.HomeAPI.as_view(), name="home"),
    path("about/", views.AboutAPI.as_view(), name="about"),
    path("services/", views.ServicesAPI.as_view(), name="services"),
    path("testimonials/", testimonial_list, name="testimonials-list"),
    path("testimonials/<int:pk>/", testimonial_detail, name="testimonials-detail"),
    path("gallery/", views.GalleryListAPI.as_view(), name="gallery-list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)