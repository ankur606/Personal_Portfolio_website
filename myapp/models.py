from django.db import models
from django.contrib.auth.models import User
class AccountsUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(unique=True, max_length=15)
    is_active = models.IntegerField()
    is_admin = models.IntegerField()
    is_superuser = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Accounts_user'


class FoodCategories(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category_name=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class FoodName(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category_name=models.ForeignKey(FoodCategories,on_delete=models.CASCADE,null=True, related_name="category")
    food_name=models.CharField(max_length=200,null=True,blank=True)
    food_image=models.ImageField(upload_to='food_image',null=True,blank=True)
    full_price=models.CharField(max_length=200,null=True,blank=True,default='-')
    medium_price=models.CharField(max_length=200,null=True,blank=True,default='-')
    small_price=models.CharField(max_length=200,null=True,blank=True,default='-')
    created_at=models.DateTimeField(auto_now_add=True)
    

    