# Generated by Django 3.2.5 on 2021-07-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.TextField(blank=True, default=None, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(blank=True, default=None, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='service',
            field=models.TextField(blank=True, default=None, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.TextField(blank=True, default=None, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='appointmentdate',
            field=models.TextField(blank=True, default=None, max_length=20000, null=True),
        ),
    ]