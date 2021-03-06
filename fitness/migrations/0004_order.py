# Generated by Django 3.0 on 2022-03-30 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness', '0003_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('order_Items', jsonfield.fields.JSONField()),
                ('itemLen', jsonfield.fields.JSONField()),
                ('price', jsonfield.fields.JSONField()),
                ('amount', models.IntegerField(default=0)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=15)),
                ('payment_method', models.CharField(default='COD', max_length=15)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
