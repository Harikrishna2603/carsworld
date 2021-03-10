# Generated by Django 3.1.5 on 2021-03-04 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_sellcar_isfav'),
    ]

    operations = [
        migrations.CreateModel(
            name='favv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sellcar')),
            ],
        ),
    ]
