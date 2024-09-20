# Generated by Django 5.1.1 on 2024-09-05 15:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('username', models.CharField(default='none', max_length=65)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(default='none', max_length=20)),
                ('last_name', models.CharField(default='none', max_length=20)),
                ('age', models.DateField(null=True)),
                ('pronouns', models.JSONField(default=dict)),
                ('records', models.JSONField(default=dict)),
                ('facts', models.JSONField(default=dict)),
                ('region', models.CharField(default='none', max_length=50)),
                ('ImgUrl', models.CharField(default='none', max_length=255)),
                ('extra_data', models.JSONField(default=dict)),
                ('user_settings', models.JSONField(default=dict)),
                ('image_collection', models.JSONField(default=dict)),
            ],
        ),
    ]