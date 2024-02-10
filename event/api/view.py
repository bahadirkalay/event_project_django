from rest_framework.filters import SearchFilter
from rest_framework import generics

from event.api.serializers import EventSerializer
from event.model import EventModel


class EventApiView(generics.ListCreateAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter]
    search_fields = ['event_name']


