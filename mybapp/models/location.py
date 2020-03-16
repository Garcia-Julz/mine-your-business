from django.db import models
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

class Location(models.Model):

    city = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("city")
        verbose_name_plural = ("cities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_detail", kwargs={"pk": self.pk})
