# Generated by Django 4.0.5 on 2022-06-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_article_amount_alter_article_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='cars'),
        ),
        migrations.AlterField(
            model_name='article',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
