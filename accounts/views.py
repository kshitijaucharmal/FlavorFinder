from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import FoodData

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def food_data_list(request):
    food_items = FoodData.objects.all()  # Get all food items
    paginator = Paginator(food_items, 10)  # Show 10 food items per page

    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the items for the current page

    # Preprocess the cleaned ingredients into a list
    for food in page_obj:
        food.cleaned_ingredients_list = food.Cleaned_Ingredients.split(',')
        food.instructions_list = food.Instructions.split('. ')

    return render(request, 'food_data_list.html', {'page_obj': page_obj})
