# Generated by Django 3.0.5 on 2020-04-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_program_career_prospectus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='career_prospectus',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='program',
            name='desc',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(default='N/A', max_length=10),
        ),
    ]
