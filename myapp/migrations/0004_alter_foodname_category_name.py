# Generated by Django 4.0.4 on 2023-04-03 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_foodcategories_user_id_alter_foodname_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodname',
            name='category_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='myapp.foodcategories'),
        ),
    ]
