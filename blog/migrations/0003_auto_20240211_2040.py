# Generated by Django 3.2.18 on 2024-02-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240128_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image5',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
