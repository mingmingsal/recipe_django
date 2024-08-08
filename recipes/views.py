from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Recipe

class IndexView(generic.ListView):
    template_name = "recipes/index.html"
    context_object_name = "recipe_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Recipe.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/details.html"

