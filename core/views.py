from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Home, About, Service, Testimonails, Gallery
from django.http import JsonResponse
from .serializers import (
    HomeSerializer,
    AboutSerializer,
    ServicesSerializer,
    TestimonialSerializer,
    GallerySerializer,
)


def root_view(request):
    return JsonResponse({"status": "ok", "message": "Backend is running"})


class HomeAPI(APIView):
    def get(self, request):
        home = Home.objects.all()
        serializer = HomeSerializer(home, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutAPI(APIView):
    def get(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServicesAPI(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServicesSerializer(
            services, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestimonialsAPI(viewsets.ModelViewSet):
    queryset = Testimonails.objects.all().order_by("-created_at")
    serializer_class = TestimonialSerializer


class GalleryListAPI(generics.ListCreateAPIView):
    queryset = Gallery.objects.all().order_by("-created_at")
    serializer_class = GallerySerializer
