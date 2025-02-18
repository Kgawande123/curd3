# Generated by Django 5.0.6 on 2024-06-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=23)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=34)),
            ],
        ),
    ]
