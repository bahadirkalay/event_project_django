from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from event.model import EventModel


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class EventSerializer(serializers.ModelSerializer):
    created_user = UserSerializers()

    class Meta:
        model = EventModel
        fields = '__all__'
