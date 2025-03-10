from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models import Avg


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
    
    @property
    def average_rating(self):
        return self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],  # Ratings from 1 to 5
        help_text="Rate the recipe from 1 (worst) to 5 (best)."
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("recipe", "user")  # Prevents a user from reviewing the same recipe multiple times

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title} ({self.rating}/5)"




