from django.db import models

class Location(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("location")
        verbose_name_plural = ("locations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location_detail", kwargs={"pk": self.pk})
