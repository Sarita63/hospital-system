# Generated by Django 4.0.4 on 2022-06-12 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_carts_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('slug', models.TextField(max_length=400)),
                ('quantity', models.IntegerField(default=1)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.products')),
            ],
        ),
        migrations.DeleteModel(
            name='Carts',
        ),
    ]
