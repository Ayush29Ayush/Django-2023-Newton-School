from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# def home(request):
#     return HttpResponse("""<h1>Hey, I am a Django server.</h1>
#                            <p> This is a para </p>
#                            <br>
#                            <p> This is para 2 </p>""")
def home(request):
    peoples = [
        {"name": "Ayush", "age": 22},
        {"name": "Senapati", "age": 23},
        {"name": "Senpai", "age": 21},
        {"name": "AngryBaka", "age": 22},
        {"name": "AngryBaka1", "age": 17},
    ]

    # peoples = [('7645693430', 'Odisha Train Accident Report Released For The First Time, Spells Out Lapse', 'train'), ('7645693430', 'Odisha Train Accident Report Released For The First Time, Spells Out Lapse', 'train'), ('7645693430', 'Odisha Train Accident Report Released For The First Time, Spells Out Lapse', 'train')]

    # for people in peoples:
    #     print(people)

    text = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum minima id quibusdam earum sint modi vero incidunt nostrum ad! Totam, tempora est ipsam libero quas reprehenderit vero asperiores esse voluptate laudantium rem dolorum. Asperiores voluptates quae, tenetur dolore laudantium inventore animi atque quos omnis. Id aspernatur sint pariatur sed. Nulla totam modi quibusdam fugiat ut inventore impedit deserunt necessitatibus nobis cum ullam quasi maxime exercitationem, est commodi odit eligendi maiores ratione magnam minus ipsam amet vitae itaque aspernatur. Voluptate rerum distinctio maxime vero quae a sapiente libero, officiis quo quidem? Corrupti nam impedit porro enim perferendis magni ullam sit aliquid!
    """

    vetetables = ["pumpkin", "tomato", "potato"]

    return render(
        request,
        "index.html",
        context={"peoples": peoples, "text": text, "vetetables": vetetables},
    )


def success_page(request):
    print("*" * 20)
    return HttpResponse("<h1>Hey, This is a success page.</h1>")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
