# Generated by Django 4.1.3 on 2023-03-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_id', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
    ]
