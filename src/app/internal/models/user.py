from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=32, null=True, unique=True)
    id = models.BigIntegerField(primary_key=True)
    phone = models.CharField(max_length=12, blank=True)
    favourites = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return f"{self.username or self.first_name}"
