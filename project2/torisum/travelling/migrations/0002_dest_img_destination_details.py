# Generated by Django 5.0.2 on 2024-06-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dest_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img', models.ImageField(upload_to='media')),
                ('bg_img2', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Destination_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_place', models.CharField(max_length=200)),
                ('des_img', models.ImageField(upload_to='media')),
                ('place_descrip', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]