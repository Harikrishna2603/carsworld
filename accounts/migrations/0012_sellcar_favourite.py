# Generated by Django 3.1.5 on 2021-03-02 05:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210225_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellcar',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourtie', to=settings.AUTH_USER_MODEL),
        ),
    ]
