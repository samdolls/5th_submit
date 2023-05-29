from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length = 20, null = False, blank = False)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField()
    hamster = models.CharField(null=True, max_length = 500)
    weather = models.CharField(null=True, max_length = 50)
    image = models.ImageField(upload_to = 'post/', blank=True, null=True)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name = 'posts', blank = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
    
class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE, blank = False, null = False)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, blank = False, null = False)
    tags = models.ManyToManyField(Tag, related_name='comments', blank = True)

    def __str__(self):
        return self.post.title + " : " + self.content[:20]
    

