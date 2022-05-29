# Generated by Django 3.2.8 on 2022-05-19 19:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otps',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('expire_at', models.DateTimeField(blank=True, null=True)),
                ('is_otp_authenticated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_otp',
            },
        ),
    ]
