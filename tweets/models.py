from django.db import models


class Author(models.Model):
    screen_name = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    profile_image_url = models.URLField()

    def serialize(self):
        return {
            'screen_name': self.screen_name,
            'name': self.screen_name,
            'profile_image_url': self.profile_image_url
        }

    def __str__(self):
        return self.screen_name


class Tweet(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField(null=True)
    text = models.CharField(max_length=255, default='', null=True)

    author = models.ForeignKey(Author, db_column='author_screen_name')
    retweeted_by = models.ManyToManyField(Author, related_name='retweeted_by')
    original_tweet = models.ForeignKey('self', null=True)
    # entities (?)
    # commands
    # preview_image_url

    def serialize(self):
        serialized_tweet = {
            'id': self.id,
            'created_at': self.created_at.ctime(),
            'favorite_count': self.favorite_count,
            'text': self.text,
            'author': self.author.serialize()
        }

        if self.original_tweet is not None:
            serialized_tweet['original_tweet'] = self.original_tweet.serialize()
        else:
            serialized_tweet['retweeted_by'] = [author.serialize() for author in self.retweeted_by.all()]

        return serialized_tweet


    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']

