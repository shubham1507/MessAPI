# Generated by Django 2.2 on 2021-02-10 08:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
            ],
        ),
    ]
