# Generated by Django 2.1.5 on 2019-02-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(),
        ),
    ]
