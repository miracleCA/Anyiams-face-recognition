# Generated by Django 4.1.5 on 2023-06-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Detection', '0003_rename_name_userprofile_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(max_length=200),
        ),
    ]
