# Generated by Django 5.0.2 on 2024-05-30 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0006_alter_history_games_id'),
        ('games', '0003_games_bg_img_games_sub_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='games_id',
        ),
        migrations.AddField(
            model_name='history',
            name='games',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='downloaded_history', to='games.games'),
        ),
    ]
