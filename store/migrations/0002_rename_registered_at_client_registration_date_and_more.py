# Generated by Django 5.1.2 on 2024-11-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='registered_at',
            new_name='registration_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
    ]
