# Generated by Django 4.1.7 on 2023-03-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cart_image',
            field=models.ImageField(upload_to='photos/categories'),
        ),
    ]
