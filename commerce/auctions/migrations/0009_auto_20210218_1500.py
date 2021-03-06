# Generated by Django 3.1.5 on 2021-02-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210218_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='user',
            field=models.CharField(default='anil', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.CharField(default='anil', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.CharField(default='anil', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]
