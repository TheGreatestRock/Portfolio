# Generated by Django 5.0.6 on 2024-06-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0012_glossaryterm_remove_image_text_field_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="name",
            field=models.CharField(default="test", max_length=100),
            preserve_default=False,
        ),
    ]