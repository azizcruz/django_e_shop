# Generated by Django 2.1.5 on 2019-01-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
