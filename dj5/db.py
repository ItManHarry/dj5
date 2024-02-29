from django.db import models
import uuid
from django.utils import timezone

class DgBaseModel(models.Model):
    class Meta:
        abstract = True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)