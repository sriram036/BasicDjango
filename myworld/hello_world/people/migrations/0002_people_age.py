# Generated by Django 4.1.6 on 2023-02-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
