# Generated by Django 5.0.2 on 2024-05-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='category',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
