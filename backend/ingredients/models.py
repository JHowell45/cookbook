from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/ingredients/')

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price}"