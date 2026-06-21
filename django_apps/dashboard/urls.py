from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_login, name="dashboard-login"),
    path("portal/", views.dashboard_home, name="dashboard-home"),
    path("portal/logout/", views.dashboard_logout, name="dashboard-logout"),
    path("portal/home/", views.dashboard_home_edit, name="dashboard-home-edit"),
    path("portal/about/", views.dashboard_about_edit, name="dashboard-about-edit"),
    path("portal/services/", views.dashboard_services, name="dashboard-services"),
    path("portal/services/<int:pk>/delete/", views.dashboard_service_delete, name="dashboard-service-delete"),
    path("portal/testimonials/", views.dashboard_testimonials, name="dashboard-testimonials"),
    path("portal/testimonials/<int:pk>/delete/", views.dashboard_testimonial_delete, name="dashboard-testimonial-delete"),
    path("portal/blog/", views.dashboard_blog, name="dashboard-blog"),
    path("portal/blog/<int:pk>/delete/", views.dashboard_blog_delete, name="dashboard-blog-delete"),
    path("portal/projects/", views.dashboard_projects, name="dashboard-projects"),
    path("portal/projects/<int:pk>/delete/", views.dashboard_project_delete, name="dashboard-project-delete"),
    path("portal/gallery/", views.dashboard_gallery, name="dashboard-gallery"),
    path("portal/gallery/<int:pk>/delete/", views.dashboard_gallery_delete, name="dashboard-gallery-delete"),
    path("portal/messages/", views.dashboard_messages, name="dashboard-messages"),
]
