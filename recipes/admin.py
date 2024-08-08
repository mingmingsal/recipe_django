from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Recipe, Ingredient

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["recipe_name"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [IngredientInline]


admin.site.register(Recipe, RecipeAdmin)
