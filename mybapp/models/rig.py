from django.db import models
from .location import Location
from .miner import Miner
# from django.contrib.auth.models import User

class Rig(models.Model):

    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    miner = models.ForeignKey(Miner, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("rig")
        verbose_name_plural = ("rigs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rig_detail", kwargs={"pk": self.pk})

