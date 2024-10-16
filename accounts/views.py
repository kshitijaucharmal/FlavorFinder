from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodData
from django.contrib import messages

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

def search_food_item(request):
    # Get the search query from the URL
    search_query = request.GET.get('search', '')

    # Filter food items based on the search query, if it exists
    if search_query:
        food_items = FoodData.objects.filter(Title__contains=search_query)  # Adjust 'Title' to your actual model field name
    else:
        food_items = FoodData.objects.all()  # Get all food items if no search query

    paginator = Paginator(food_items, 10)  # Show 10 food items per page

    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the items for the current page

    # Preprocess the cleaned ingredients into a list
    for food in page_obj:
        food.cleaned_ingredients_list = food.Cleaned_Ingredients.split(',')
        food.instructions_list = food.Instructions.split('. ')

    return render(request, 'food_data_list.html', {
        'page_obj': page_obj,
        'search_query': search_query  # Pass the search query to the template for retaining the input
    })

def update_food(request, serial_no):
    food_item = get_object_or_404(FoodData, SerialNo=serial_no)
    
    if request.method == "POST":
        food_item.Title = request.POST.get('title')  # Update Title
        food_item.Instructions = request.POST.get('instructions')  # Update Instructions
        food_item.Image_Name = "Null"
        food_item.Cleaned_Ingredients = request.POST.get('cleaned_ingredients')  # Update Cleaned_Ingredients
        food_item.save()  # Save the updated record to the database
        messages.success(request, 'Food item updated successfully!')
        return redirect('food_data_list', serial_no=food_item.SerialNo)  # Redirect to detail view or list

    return render(request, 'update_food.html', {'food_item': food_item})  # Render update form

def delete_food(request, serial_no):
    food_item = get_object_or_404(FoodData, SerialNo=serial_no)
    
    if request.method == "POST":
        food_item.delete()  # Delete the record from the database
        messages.success(request, 'Food item deleted successfully!')
        return redirect('food_data_list')  # Redirect to your food list view

    return render(request, 'confirm_delete.html', {'food_item': food_item})  # Render confirmation page
