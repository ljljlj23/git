# Generated by Django 2.2.1 on 2019-09-11 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_id',
            new_name='publish',
        ),
    ]