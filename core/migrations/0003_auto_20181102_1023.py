# Generated by Django 2.1.2 on 2018-11-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181102_1009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['priority', 'percent']},
        ),
        migrations.AddField(
            model_name='project',
            name='percent',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=10),
        ),
    ]