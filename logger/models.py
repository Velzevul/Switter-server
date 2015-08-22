from django.db import models


class Log(models.Model):
    participant_id = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255, default='***')

    def __str__(self):
        return self.message