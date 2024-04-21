from rest_framework.response import Response
from rest_framework import viewsets, permissions, request, status
from urls.models import Collection, Url
from urls.serializers import CollectionSerializer, UrlSerializer
from users.models import User


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super(CollectionViewSet, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super(UrlViewSet, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

