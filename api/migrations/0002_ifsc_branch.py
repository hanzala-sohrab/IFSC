# Generated by Django 3.0.3 on 2020-07-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ifsc',
            name='BRANCH',
            field=models.CharField(default='Foo', max_length=100),
        ),
    ]
