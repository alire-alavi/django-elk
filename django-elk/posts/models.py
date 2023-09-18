from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.title

