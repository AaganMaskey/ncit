# Generated by Django 3.0.5 on 2020-04-15 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]