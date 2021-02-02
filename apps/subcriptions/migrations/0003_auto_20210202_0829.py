# Generated by Django 2.2 on 2021-02-02 08:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subcriptions', '0002_auto_20210103_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersubscription',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
