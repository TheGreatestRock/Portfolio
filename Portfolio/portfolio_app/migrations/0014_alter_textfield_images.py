# Generated by Django 5.0.6 on 2024-06-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0013_image_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="textfield",
            name="images",
            field=models.ManyToManyField(blank=True, to="portfolio_app.image"),
        ),
    ]
