from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/recipes/login/")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        # print(recipe_name)
        # print(recipe_description)
        # print(recipe_image)

        # This adds a new entry to the database
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect("/recipes/")

    queryset = Recipe.objects.all()

    if request.GET.get("search_recipe"):
        # print(request.GET.get('search_recipe'))
        queryset = queryset.filter(
            recipe_name__icontains=request.GET.get("search_recipe")
        )

    context = {"recipes": queryset}

    return render(request, "recipes.html", context)

@login_required(login_url="/recipes/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect("/recipes/")

    context = {"recipe": queryset}
    return render(request, "update_recipes.html", context)

@login_required(login_url="/recipes/login/")
def delete_recipe(request, id):
    # print("The id passed is", id)
    # return HttpResponse("delete_recipe view executed...")
    queryset = Recipe.objects.get(id=id)
    queryset.delete()

    return redirect("/recipes/")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect("/recipes/login/")

        # agar issi username aur password ke saath authenticate ho gaya toh uss user ka object return kar dega else None return karega
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/recipes/login/")
        else:
            login(
                request, user
            )  # this will login the user and manage the session of this user
            return redirect("/recipes/")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/recipes/login/")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect("/recipes/register/")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            # password=password,
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully...")

        return redirect("/recipes/register/")

    return render(request, "register.html")
