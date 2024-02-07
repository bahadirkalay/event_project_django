from django.db import models

from event.model.base_model import BaseModel


# Create your models here.

class EventModel(BaseModel):
    event_name = models.CharField(max_length=120, null=False, blank=False, verbose_name="Etkinlik Başlığı")
    event_description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Etkinlik Kısa Açıklama")
    event_body = models.TextField(null=False, blank=False, verbose_name="Etkinlik Hakkında")
    event_start_time = models.DateTimeField(null=False, blank=False, verbose_name="Başlangıç Tarih ve Saat")
    event_image = models.ImageField(upload_to='images/')
    event_end_time = models.DateTimeField(null=False, blank=False, verbose_name="Bitiş Tarih ve Saat")
    event_latitude = models.CharField(max_length=10, null=False, blank=False, verbose_name="Enlem")
    event_longitude = models.CharField(max_length=10, null=False, blank=False, verbose_name="Boylam")
    event_isActive = models.BooleanField(default=False, verbose_name="Aktif/Pasif")
    event_isPublish = models.BooleanField(default=False, verbose_name="Yayın Durumu")
