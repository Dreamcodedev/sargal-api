# Generated by Django 4.0.5 on 2022-06-29 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_article_price_promotion_article_promotion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='price_promotion',
        ),
    ]
