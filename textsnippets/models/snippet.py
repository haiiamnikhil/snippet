import uuid

from django.db import models

from users.models.users import Users
from textsnippets.models.tags import Tags


class Snippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False, null=False, related_name='snippet_user')
    title = models.CharField(max_length=50, unique=False, blank=False, null=False)
    snippet = models.TextField(max_length=250, null=False, blank=False)
    tag = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True, blank=False, related_name='snippet_tag')
    created_at = models.DateTimeField(auto_now_add=True)

    object = models.Manager()

    class Meta:
        verbose_name_plural = 'snippet'

    def __str__(self):
        return str(self.title)
