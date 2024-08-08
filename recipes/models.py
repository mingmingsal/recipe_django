from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.CharField(max_length=1024)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)
    measure_unit = models.CharField(max_length=3)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return self.ingredient_name
    def is_meat(self): 
        meat_strings = ['pork','beef','sausage','chicken'] 
        #test meats (could probably make it so that ingredients can have other ingredients, going down to base animals, then test for all)
        if self.ingredient_name in meat_strings:
            return True
        return False