# Generated by Django 2.1.3 on 2019-05-01 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190501_1941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-posted']},
        ),
    ]
