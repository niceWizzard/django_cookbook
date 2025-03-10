from django import forms
from recipes.models import Recipe, Review

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["image", "title", "tags", "recipe"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment",]