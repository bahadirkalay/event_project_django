from django.urls import path, include

from event.api.view import EventApiView

app_name = 'event_api'
urlpatterns = [
    path('list', EventApiView.as_view(), name='list')

]
