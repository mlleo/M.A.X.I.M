# Generated by Django 2.2.2 on 2019-06-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0009_auto_20190608_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation_id',
            field=models.IntegerField(default=0),
        ),
    ]
