# Generated by Django 4.2.2 on 2023-06-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
