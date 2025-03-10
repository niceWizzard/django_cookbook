from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=True,null=True)
    title = models.CharField(max_length=72)
    tags = models.CharField(max_length=256)
    recipe = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)