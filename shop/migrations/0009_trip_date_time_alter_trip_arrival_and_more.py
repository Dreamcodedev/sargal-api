# Generated by Django 4.0.5 on 2022-06-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='date_time',
            field=models.CharField(default='gggg', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='arrival',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='departure',
            field=models.CharField(max_length=255),
        ),
    ]
