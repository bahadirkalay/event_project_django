from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from event.api.serializers import EventSerializer, EventDetailSerializers
from event.model import EventModel


class EventApiView(ListCreateAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter]
    search_fields = ['event_name']


class EventApiDetailView(RetrieveAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventDetailSerializers
    lookup_field = "pk"
