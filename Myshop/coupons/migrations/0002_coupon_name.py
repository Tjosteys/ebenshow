# Generated by Django 3.0.5 on 2020-08-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='name',
            field=models.CharField(default='Welcome', max_length=50),
            preserve_default=False,
        ),
    ]
