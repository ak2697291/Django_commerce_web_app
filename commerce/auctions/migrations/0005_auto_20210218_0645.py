# Generated by Django 3.1.5 on 2021-02-18 01:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='user',
        ),
        migrations.AddField(
            model_name='bid',
            name='starting_bid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='data',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='auctions.auction_listing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='title',
            field=models.CharField(max_length=65),
        ),
    ]
