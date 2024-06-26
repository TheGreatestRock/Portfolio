# Generated by Django 5.0.6 on 2024-06-04 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ApprentissageCritique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apprentissages_critiques', to='portfolio_app.competence')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='competences',
            field=models.ManyToManyField(blank=True, to='portfolio_app.competence'),
        ),
    ]
