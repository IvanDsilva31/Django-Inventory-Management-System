# Generated by Django 4.0.4 on 2023-04-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='Profile_Images'),
        ),
    ]
