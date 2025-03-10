from django.urls import  path

from recipes.views import create_page, create_review, delete_route, edit_page, list_page, recipe_page


app_name = "recipes"

urlpatterns = [
    path("create/", create_page, name="create"),
    path("edit/<str:id>/", edit_page, name="edit"),
    path("", list_page, name="list"),
    path("<str:id>/", recipe_page),
    path("<str:id>/delete/", delete_route, name='delete'),
    path("<str:id>/review/", create_review, name='create-review'),
]

