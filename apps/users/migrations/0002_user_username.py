# Generated by Django 3.1.4 on 2021-01-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=40, unique=True),
            preserve_default=False,
        ),
    ]