# Generated by Django 5.0.6 on 2024-06-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_delete_additionalpage_delete_pageinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('skills', models.JSONField()),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
                ('social_links', models.JSONField()),
            ],
        ),
    ]
