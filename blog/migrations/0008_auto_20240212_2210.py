# Generated by Django 3.2.18 on 2024-02-12 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_image5_post_image0'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image0',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image1',
            new_name='image5',
        ),
    ]
