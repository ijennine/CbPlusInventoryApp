# Generated by Django 3.1.3 on 2020-11-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('reference', models.AutoField(primary_key=True, serialize=False)),
                ('product_gtin', models.IntegerField()),
                ('expiration_date', models.DateField()),
            ],
        ),
    ]
