# Generated by Django 5.0.6 on 2024-06-12 19:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0015_image_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="end",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="start",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
