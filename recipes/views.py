from django.http import HttpRequest, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from recipes.forms import RecipeForm

def list_page(req: HttpRequest):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        recipe.tags_list = recipe.tags.split(',')
    return render(req, "recipes/recipe_list.html", {"recipes": recipes})

@login_required
def create_page(req: HttpRequest):
    form = RecipeForm()
    if req.method == "POST":
        form = RecipeForm(req.POST, req.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = req.user  # Assign the logged-in user
            recipe.save()
            return HttpResponseRedirect("/")  # Redirect to home or list page
    return render(req, "recipes/create_recipe.html", {"form": form})

@login_required
def edit_page(req: HttpRequest, id: str):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.author != req.user:
        return HttpResponseForbidden("You are not allowed to do that.")
    form = RecipeForm(instance=recipe)
    if req.method == "POST":
        form = RecipeForm(req.POST, req.FILES, instance=recipe)
        if form.is_valid():
            recipe.save()
            return redirect(f"/recipes/{id}") 
    return render(req, "recipes/edit_recipe.html", {"form": form})

def recipe_page(req : HttpRequest, id: str):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.tags_list = recipe.tags.split(',')
    return render(req, 'recipes/recipe.html', {'recipe':recipe})