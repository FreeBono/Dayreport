# Generated by Django 3.2.9 on 2021-12-16 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_auto_20211216_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='setls',
            field=models.TextField(null=True),
        ),
    ]