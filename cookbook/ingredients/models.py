from django.db import models
from core.database.mixins import DateAndTimeMixin

# Create your models here.
class Ingredient(DateAndTimeMixin, models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=False)

    def __str__(self) -> str:
        return f" {self.id}, {self.name=}, {self.description=}"