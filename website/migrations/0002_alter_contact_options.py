# Generated by Django 3.2.22 on 2023-10-26 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-created_date',)},
        ),
    ]
