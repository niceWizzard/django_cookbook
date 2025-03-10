from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True,null=True)
    title = models.CharField(
        max_length=72,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9\s]+$',  # Only letters, numbers, and spaces
                message="Title can only contain letters, numbers, and spaces.",
                code="invalid_title"
            )
        ]
    )
    tags = models.CharField(
        max_length=256,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+(,[a-zA-Z]+)*$',  # Letters only, comma-separated, no spaces
                message="Tags must be comma-separated words with only letters (e.g., 'pancakes,breakfast,delicious')."
            )
        ]
    )
    recipe = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)