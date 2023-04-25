from django.shortcuts import render


def index(request, *args):
    return render(request, "menu/index.html")


def other_page(request, *args):
    return render(request, "menu/other_page.html")
