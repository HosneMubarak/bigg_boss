# Generated by Django 3.1 on 2020-08-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_article_ad_part_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]