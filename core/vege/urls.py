from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipes, name="recipeshome"),
    path("delete-recipe/<int:id>/", views.delete_recipe, name="delete_recipe"),
    path("update-recipe/<int:id>/", views.update_recipe, name="update_recipe"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout_page"),
    path("register/", views.register_page, name="register_page"),
]
