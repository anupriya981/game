# Generated by Django 5.0.2 on 2024-06-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelling', '0002_dest_img_destination_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tra_img', models.ImageField(upload_to='media')),
                ('tra_des', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='destination_details',
            name='place_descrip',
            field=models.CharField(max_length=500),
        ),
    ]
