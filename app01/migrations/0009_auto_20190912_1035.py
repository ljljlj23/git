# Generated by Django 2.2.1 on 2019-09-12 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_teacher_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
