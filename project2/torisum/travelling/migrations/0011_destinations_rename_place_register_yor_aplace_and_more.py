# Generated by Django 5.0.2 on 2024-09-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelling', '0010_visitplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_place_visit', models.TextField(max_length=1000)),
                ('name_visit', models.CharField(max_length=100)),
                ('img_visit', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.RenameField(
            model_name='register',
            old_name='place',
            new_name='yor_aplace',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='des_place_visit1',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='des_place_visit2',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='des_place_visit3',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='des_place_visit4',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='des_place_visit5',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='des_place_visit6',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='img_visit1',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='img_visit2',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='img_visit3',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='img_visit4',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='img_visit5',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='img_visit6',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='name_visit1',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='name_visit2',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='name_visit3',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='name_visit4',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='name_visit5',
        ),
        migrations.RemoveField(
            model_name='destination_details',
            name='name_visit6',
        ),
    ]