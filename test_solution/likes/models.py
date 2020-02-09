from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    body = models.CharField(max_length=10000, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    date_published = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    likes = models.BigIntegerField(null=True, blank=True, default=0)
    dislikes = models.BigIntegerField(null=True, blank=True, default=0)

    POST_TYPES= (
        ('p', 'Post'),
        ('n', 'News')
    )

    post_type = models.CharField(max_length=1,
                                 choices=POST_TYPES,
                                 blank=True,
                                 null=True,
                                 help_text='Is it news or post?',
                                 default='n')

    def __str__(self):
        return self.subject

    @property
    def all_marks(self):
        return self.likes + self.dislikes







