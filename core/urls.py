from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import TestimonialsAPI

router = DefaultRouter()
router.register(r'api/testimonials', TestimonialsAPI, basename='testimonials')

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
    path("home/", views.HomeAPI.as_view(), name="home-clean"),
    path("about/", views.AboutAPI.as_view(), name="about-clean"),
    path("services/", views.ServicesAPI.as_view(), name="services-clean"),
    path("testimonials/", testimonial_list, name="testimonials-list-clean"),
    path("testimonials/<int:pk>/", testimonial_detail, name="testimonials-detail-clean"),
    path("gallery/", views.GalleryListAPI.as_view(), name="gallery-list-clean"),
]

# add router urls
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)