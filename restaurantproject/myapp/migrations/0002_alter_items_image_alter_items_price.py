# Generated by Django 5.0.7 on 2024-12-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(upload_to='items/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='Price',
            field=models.TextField(max_length=30),
        ),
    ]
