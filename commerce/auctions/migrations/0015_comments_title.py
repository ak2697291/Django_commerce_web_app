# Generated by Django 3.1.5 on 2021-02-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210219_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='title',
            field=models.CharField(default='OPPO F3 Plus Data cable', max_length=64),
            preserve_default=False,
        ),
    ]
