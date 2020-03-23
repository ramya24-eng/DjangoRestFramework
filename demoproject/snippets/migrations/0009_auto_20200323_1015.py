# Generated by Django 2.1.7 on 2020-03-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20200323_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
