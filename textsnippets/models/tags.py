import uuid

from django.db import models


class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=20, unique=True, blank=False, null=False)

    object = models.Manager()

    class Meta:
        verbose_name_plural = 'tag'

    def __str__(self):
        return str(self.title)
