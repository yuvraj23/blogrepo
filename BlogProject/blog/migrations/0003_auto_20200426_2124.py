# Generated by Django 3.0.5 on 2020-04-26 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='updated',
        ),
    ]
