# Generated by Django 5.0 on 2024-04-30 06:49

import datetime
import django.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2024, 4, 30, 9, 49, 37, 81443))),
            ],
        ),
        migrations.CreateModel(
            name='GymMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(default='0900000000', max_length=14)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='upload/profile')),
                ('joinedAt', models.DateTimeField()),
                ('payedAt', models.DateTimeField(default=datetime.datetime(2024, 4, 30, 9, 49, 37, 81443))),
                ('active', models.BooleanField(default=True)),
                ('plan', models.OneToOneField(on_delete=django.db.models.fields.CharField, to='gymManagement.plan')),
            ],
        ),
    ]
