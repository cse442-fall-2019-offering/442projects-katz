# Generated by Django 2.2.6 on 2019-11-07 07:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0011_auto_20191020_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together={('name', 'school', 'start_time', 'end_time', 'professor_name')},
        ),
    ]
