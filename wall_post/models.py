from __future__ import unicode_literals

from django.db import models


class WallPost(models.Model):

    name = models.CharField(max_length=50)
    post = models.CharField(max_length=500)

    def __str__(self):
        return self.name
