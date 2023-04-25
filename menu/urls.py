from django.urls import path, re_path

from menu import views

urlpatterns = [
    path("", views.index, name="index"),
    path("some-other-path/", views.other_page, name="menu-named-path"),
    re_path(r"^(.*)/$", views.index, name="index"),
]
