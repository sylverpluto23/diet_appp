# Generated by Django 3.1.7 on 2021-04-20 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietplan', '0004_auto_20210420_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfomodel',
            old_name='height',
            new_name='height_in_cm',
        ),
    ]
