# Generated by Django 3.0.5 on 2020-05-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_auto_20200416_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='code',
            field=models.IntegerField(),
        ),
    ]
