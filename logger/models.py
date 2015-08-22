from django.db import models


class Log(models.Model):
    participant_id = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255, default='***')

    def __str__(self):
        return self.message


class Journal(models.Model):
    participant_id = models.CharField(max_length=255)
    created_at = models.CharField(max_length=255, default='***')
    interesting_tweets_found = models.CharField(max_length=255)
    interesting_tweets_description = models.CharField(max_length=255)
    new_things_learnt = models.CharField(max_length=255)
    new_things_description = models.CharField(max_length=255)
    free_form_feedback = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{0} | {1}".format(self.created_at, self.participant_id)