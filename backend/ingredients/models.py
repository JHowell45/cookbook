from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.IntegerField()
    unit = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/ingredients/')

    def __str__(self):
        return self.name