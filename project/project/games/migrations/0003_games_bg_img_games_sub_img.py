# Generated by Django 5.0.2 on 2024-05-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_games_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='bg_img',
            field=models.ImageField(default=1, upload_to='media/bg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='sub_img',
            field=models.ImageField(default=1, upload_to='media/sub'),
            preserve_default=False,
        ),
    ]
