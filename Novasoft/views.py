from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from Novasoft.models import Developer, Contact
from Novasoft.serializers import DeveloperSerializer, ContactSerializer


class DeveloperAPIViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # for search into developers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class ContactAPIViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
