# Generated by Django 5.0.2 on 2024-05-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0005_remove_downloaded_items_games_id_history_games_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='games_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
