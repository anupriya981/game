# Generated by Django 5.0.2 on 2024-09-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelling', '0009_destination_details_name_visit1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_place_visit', models.TextField(max_length=1000)),
                ('name_visit', models.CharField(max_length=100)),
                ('img_visit', models.ImageField(upload_to='media')),
            ],
        ),
    ]
