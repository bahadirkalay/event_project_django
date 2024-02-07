from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
