# Generated by Django 3.2.5 on 2021-07-21 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Blogpost',
        ),
    ]
