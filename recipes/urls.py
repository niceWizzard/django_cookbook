from django.urls import  path

from recipes.views import create_page, list_page, recipe_page


app_name = "recipes"

urlpatterns = [
    path("create/", create_page, name="create"),
    path("", list_page, name="list"),
    path("<str:id>/", recipe_page)
]

