# Generated by Django 3.2.18 on 2024-02-12 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20240212_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image5',
        ),
    ]