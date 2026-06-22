from django.contrib import admin
from .models import Home, About, Testimonails, Service, Gallery

# Register your models here.

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    list_filter = ("title",)
    search_fields = ['title']
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    list_filter = ("heading",)
    search_fields = ['heading']
    
@admin.register(Testimonails)
class TestimonailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimonial')
    list_filter = ("name",)

@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ("title",)
    search_fields = ['title']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title', 'description']