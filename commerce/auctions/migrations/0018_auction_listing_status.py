# Generated by Django 3.1.5 on 2021-02-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210219_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
