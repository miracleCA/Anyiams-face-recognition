# Generated by Django 4.1.5 on 2023-06-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Detection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='job',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
