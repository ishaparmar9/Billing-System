# Generated by Django 4.0.3 on 2022-05-01 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_bill_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.CharField(max_length=100),
        ),
    ]