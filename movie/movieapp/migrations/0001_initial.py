# Generated by Django 5.1.4 on 2025-01-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('year', models.CharField(max_length=20)),
            ],
        ),
    ]
