# Generated by Django 2.0.7 on 2018-07-21 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppinglists', '0004_shoppinglist_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
