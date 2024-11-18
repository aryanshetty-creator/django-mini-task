from django.db import models

# Create your models here.
# recipes/models.py


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the creation date

    def __str__(self):
        return self.title
