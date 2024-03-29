# Generated by Django 4.2.7 on 2024-03-16 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("order", "0003_rename_total_amount_order_amount_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="coupon",
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="order.address",
            ),
        ),
    ]
