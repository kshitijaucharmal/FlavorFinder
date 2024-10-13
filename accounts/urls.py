from django.urls import path

from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('food-data/', views.food_data_list, name='food_data_list'),
]
