from django.db import models


class Users(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    username = models.CharField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'users'
