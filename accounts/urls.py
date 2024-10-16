from django.urls import path

from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('food-data/', views.food_data_list, name='food_data_list'),
    path('search-food/', views.search_food_item, name='search_food_item'),
    path('food-data/<int:serial_no>/update/', views.update_food, name='update_food'),  # Update URL
    path('food-data/<int:serial_no>/delete/', views.delete_food, name='delete_food'),  # Delete URL
]
