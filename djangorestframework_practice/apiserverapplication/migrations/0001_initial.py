# Generated by Django 4.2.3 on 2023-07-27 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('published_date', models.DateField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
