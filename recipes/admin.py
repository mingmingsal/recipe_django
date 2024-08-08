from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Recipe, Ingredient, Step

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1
class StepInline(admin.TabularInline):
    model = Step
    extra = 1
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["recipe_name"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [IngredientInline, StepInline]


admin.site.register(Recipe, RecipeAdmin)
