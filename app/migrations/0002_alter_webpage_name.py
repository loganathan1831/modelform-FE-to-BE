# Generated by Django 4.1.4 on 2023-02-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
