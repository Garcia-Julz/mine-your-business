from django.db import models

class IssueType(models.Model):

    issue_type_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("issue_type")
        verbose_name_plural = ("issue_types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("issue_type_detail", kwargs={"pk": self.pk})
