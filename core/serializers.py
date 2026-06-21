from rest_framework import serializers
from .models import Home, About, Service, Testimonails, Gallery


class AbsoluteURLMixin:
    """
    Helper mixin to return absolute URLs for image fields (works with Cloudinary).
    """
    def get_absolute_image_url(self, request, image_field):
        if image_field and hasattr(image_field, "url"):
            return request.build_absolute_uri(image_field.url)
        return None


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer, AbsoluteURLMixin):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = "__all__"

    def get_profile_image(self, obj):
        request = self.context.get("request")
        return self.get_absolute_image_url(request, obj.profile_image)


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer, AbsoluteURLMixin):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Testimonails
        fields = "__all__"

    def get_avatar(self, obj):
        request = self.context.get("request")
        return self.get_absolute_image_url(request, obj.avatar)


class GallerySerializer(serializers.ModelSerializer, AbsoluteURLMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")
        return self.get_absolute_image_url(request, obj.image)
