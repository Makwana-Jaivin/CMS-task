from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField()
    content=models.TextField()
    creation_time=models.DateTimeField(auto_now_add=True)
    is_public=models.BooleanField(default=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} liked {self.post.title}"
