from rest_framework import generics
from hotels.models import Hotel
from hotels.api.filters import HotelFilter
from hotels.api.serializers import HotelSerializer
from django_filters.rest_framework import DjangoFilterBackend


class HotelListView(generics.ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter

