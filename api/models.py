from django.db import models


class Author(models.Model):
    screen_name = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    profile_image_url = models.URLField()

    def __str__(self):
        return self.screen_name


class Tweet(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField(null=True)
    text = models.CharField(max_length=255, default='', null=True)

    author = models.ForeignKey(Author, db_column='author_screen_name')
    retweeted_by = models.ManyToManyField(Author, related_name='retweeted_by', null=True)
    retweeted_status = models.ForeignKey('self', null=True)
    preview_image_url = models.CharField(max_length=255, default=None, null=True)
    menu_items = models.TextField(default=None, null=True)
    toolbar_items = models.TextField(default=None, null=True)
    panelbar_items = models.TextField(default=None, null=True)

    is_deployed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
