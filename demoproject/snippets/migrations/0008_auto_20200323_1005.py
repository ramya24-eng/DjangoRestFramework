# Generated by Django 2.1.7 on 2020-03-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20200323_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
