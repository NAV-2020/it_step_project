# Generated by Django 2.2.7 on 2020-11-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='upload/images/'),
        ),
    ]
