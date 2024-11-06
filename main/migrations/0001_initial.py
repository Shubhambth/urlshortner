# Generated by Django 5.1.3 on 2024-11-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_path', models.CharField(blank=True, max_length=6, unique=True)),
                ('visits', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]