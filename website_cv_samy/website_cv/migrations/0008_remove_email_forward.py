# Generated by Django 2.1.7 on 2019-04-04 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_cv', '0007_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='forward',
        ),
    ]