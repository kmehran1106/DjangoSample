# Generated by Django 3.2.7 on 2021-09-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('ipaddress', models.CharField(blank=True, default='', max_length=24)),
            ],
            options={
                'db_table': 'request_log',
            },
        ),
    ]
