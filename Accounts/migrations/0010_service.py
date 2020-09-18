# Generated by Django 3.1.1 on 2020-09-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('count_day', models.IntegerField(null=True)),
                ('count_internet', models.IntegerField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
