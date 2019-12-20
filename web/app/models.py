from django.db import models

from time import time

class Ingredient(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

class Component(models.Model):
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    dosage = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ingredient)+'-'+str(self.dosage)

class Recipe(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    # com = models.F
    component = models.ManyToManyField('Component', related_name='components')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
