# Generated by Django 5.0.6 on 2024-06-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_pageinfo_additionalpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='technologies_used',
        ),
        migrations.AddField(
            model_name='project',
            name='frameworks',
            field=models.ManyToManyField(blank=True, to='portfolio_app.framework'),
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(blank=True, to='portfolio_app.language'),
        ),
    ]
