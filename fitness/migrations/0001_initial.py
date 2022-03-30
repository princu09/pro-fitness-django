# Generated by Django 3.0 on 2022-03-30 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('usage', models.TextField()),
                ('price', models.IntegerField()),
                ('categories', models.TextField()),
                ('rating', models.IntegerField()),
                ('images1', models.ImageField(upload_to='media')),
                ('images2', models.ImageField(upload_to='media')),
                ('images3', models.ImageField(upload_to='media')),
                ('images4', models.ImageField(upload_to='media')),
                ('images5', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', jsonfield.fields.JSONField()),
                ('price', jsonfield.fields.JSONField()),
                ('items', jsonfield.fields.JSONField()),
                ('subTotal', jsonfield.fields.JSONField()),
                ('grandTotal', models.IntegerField()),
                ('address', models.TextField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemLen', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]