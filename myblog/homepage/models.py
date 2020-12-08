from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    post_image = models.ImageField(upload_to='post_images/', blank=True)
    post_text = models.CharField(max_length=300)
    post_time = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.post_text[:10]

    @property
    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.event)
