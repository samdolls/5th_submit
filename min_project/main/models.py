from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length = 50)
    pub_date = models.DateTimeField()
    hamster = models.CharField(null=True, max_length = 500)
    weather = models.CharField(null=True, max_length = 50)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
