from django.urls import  path

from project.views import homepage
from users.views import login_page, register_page

app_name = "users"

urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
]

