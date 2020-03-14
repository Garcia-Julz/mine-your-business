from django.db import models
from django.shortcuts import render, redirect, reverse

class IssueType(models.Model):

    cat = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("cat")
        verbose_name_plural = ("cats")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cat_detail", kwargs={"pk": self.pk})
