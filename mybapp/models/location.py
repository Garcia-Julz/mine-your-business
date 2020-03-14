from django.db import models
from django.shortcuts import render, redirect, reverse

class Location(models.Model):

    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("city")
        verbose_name_plural = ("cities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_detail", kwargs={"pk": self.pk})
