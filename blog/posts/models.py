from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    body = models.TextField() ## text area
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.png", blank=True)


    def __str__(self) -> str:
        return self.title