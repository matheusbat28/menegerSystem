from django.shortcuts import get_object_or_404
from .serializers import CountriesSerializer
from .models import Countries
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.db.models import Q

class CountriesViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="bisca por nome, uf ou gentilico",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def list(self, request):
        serch = request.GET.get('search', None)

        if serch:
            queryset = Countries.objects.filter(
                Q(name__icontains=serch) |
                Q(uf__icontains=serch) |
                Q(gentle__icontains=serch)
            )

        queryset = Countries.objects.all()
        serializer = CountriesSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'uf': openapi.Schema(type=openapi.TYPE_STRING),
                'gentle': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: 'OK', 400: 'Error'},
    )
    def create(self, request):
        serializer = CountriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Countries.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CountriesSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'uf': openapi.Schema(type=openapi.TYPE_STRING),
                'gentle': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: 'OK', 400: 'Error'},
    )
    def update(self, request, pk=None):
        queryset = Countries.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CountriesSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Countries.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
