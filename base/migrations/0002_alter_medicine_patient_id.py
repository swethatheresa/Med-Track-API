# Generated by Django 4.1.2 on 2022-11-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='patient_id',
            field=models.CharField(max_length=25),
        ),
    ]
