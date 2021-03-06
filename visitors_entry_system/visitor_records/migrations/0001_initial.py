# Generated by Django 2.0.3 on 2018-04-13 08:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobile_number', models.IntegerField(default=0)),
                ('details', models.TextField()),
                ('entry_time', models.DateTimeField(auto_now=True)),
                ('exit_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Visitor Detail',
                'verbose_name_plural': 'Visitors Details',
            },
        ),
    ]
