# Generated by Django 2.2.3 on 2019-08-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resanal', '0017_auto_20190817_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fetch',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
