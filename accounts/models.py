from django.db import models

# Create your models here.
class FoodData(models.Model):
    SerialNo = models.IntegerField(primary_key=True)  # Assuming 'SerialNo' is the primary key
    Title = models.CharField(max_length=100, null=True, blank=True)
    Instructions = models.CharField(max_length=800, null=True, blank=True)
    Image_Name = models.CharField(max_length=50, null=True, blank=True)
    Cleaned_Ingredients = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = 'FoodData'  # Specify the actual table name if different from the model name
