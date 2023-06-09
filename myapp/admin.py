from django.contrib import admin
from .models import FoodCategories, FoodName

@admin.register(FoodCategories)
class FoodCategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodName)
class FoodNameAdmin(admin.ModelAdmin):
    pass