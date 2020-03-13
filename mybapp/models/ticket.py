from django.db import models
from .rig import Rig
from .issue_type import IssueType
from django.contrib.auth.models import User

class Ticket(models.Model):

    title = models.CharField(max_length=50)
    comments = models.CharField(max_length=200)
    urgent = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rig = models.ForeignKey(Rig, on_delete=models.CASCADE)
    issue_type_name = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("ticket")
        verbose_name_plural = ("tickets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"pk": self.pk})