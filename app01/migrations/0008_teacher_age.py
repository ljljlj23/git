# Generated by Django 2.2.1 on 2019-09-12 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
