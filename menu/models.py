from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"[{self.menu.name}] {self.name}"
