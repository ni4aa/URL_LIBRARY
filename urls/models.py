from django.db import models

from users.models import User


class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Url(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    type = models.CharField(default="website")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ManyToManyField(Collection)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("url", "user"),)



