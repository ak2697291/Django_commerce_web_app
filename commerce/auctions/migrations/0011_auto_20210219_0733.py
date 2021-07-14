# Generated by Django 3.1.5 on 2021-02-19 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210218_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='title',
            field=models.CharField(default='OPPO F3 Plus Data cable', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='user',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.CharField(max_length=65),
        ),
    ]
