from django.urls import path, include

from event.api.view import EventApiView, EventApiDetailView

app_name = 'event_api'
urlpatterns = [
    path('list', EventApiView.as_view(), name='list'),
    path('detail/<pk>', EventApiDetailView.as_view(), name="detail")
]
