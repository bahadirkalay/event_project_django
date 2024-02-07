# Generated by Django 5.0.1 on 2024-02-07 20:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='event.basemodel')),
                ('event_name', models.CharField(max_length=120, verbose_name='Etkinlik Başlığı')),
                ('event_description', models.CharField(max_length=100, verbose_name='Etkinlik Kısa Açıklama')),
                ('event_body', models.TextField(verbose_name='Etkinlik Hakkında')),
                ('event_start_time', models.DateTimeField(verbose_name='Başlangıç Tarih ve Saat')),
                ('event_image', models.ImageField(upload_to='images/')),
                ('event_end_time', models.DateTimeField(verbose_name='Bitiş Tarih ve Saat')),
                ('event_latitude', models.CharField(max_length=10, verbose_name='Enlem')),
                ('event_longitude', models.CharField(max_length=10, verbose_name='Boylam')),
                ('event_isActive', models.BooleanField(default=False, verbose_name='Aktif/Pasif')),
                ('event_isPublish', models.BooleanField(default=False, verbose_name='Yayın Durumu')),
            ],
            bases=('event.basemodel',),
        ),
    ]
