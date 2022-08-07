# Generated by Django 4.0.4 on 2022-07-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.AlterField(
            model_name='products',
            name='labels',
            field=models.CharField(blank=True, choices=[('Heart', 'Heart'), ('Kidney', 'Kidney'), ('Gyno ', 'Gyno'), ('', 'default'), ('Eye', 'Eye'), ('Skin', 'Skin')], max_length=500),
        ),
    ]
