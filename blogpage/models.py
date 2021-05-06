from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/', blank=True)

    def get_summary(self):
        return self.text[:500] + "..."

    def __str__(self):
        return self.title
