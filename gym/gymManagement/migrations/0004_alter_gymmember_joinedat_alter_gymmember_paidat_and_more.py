# Generated by Django 5.0 on 2024-04-30 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymManagement', '0003_remove_gymmember_payedat_gymmember_paidat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymmember',
            name='joinedAt',
            field=models.DateTimeField(default=datetime.date(2024, 4, 30)),
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='paidAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 10, 17, 22, 138436)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 10, 17, 22, 138436)),
        ),
    ]
