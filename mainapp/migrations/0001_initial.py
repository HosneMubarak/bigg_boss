# Generated by Django 3.1 on 2020-08-30 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('single_video_google', models.URLField(blank=True, max_length=400, null=True)),
                ('single_video_other', models.URLField(blank=True, max_length=400, null=True)),
                ('Part_1', models.URLField(blank=True, max_length=400, null=True)),
                ('Part_2', models.URLField(blank=True, max_length=400, null=True)),
                ('Part_3', models.URLField(blank=True, max_length=400, null=True)),
                ('Part_4', models.URLField(blank=True, max_length=400, null=True)),
                ('Part_5', models.URLField(blank=True, max_length=400, null=True)),
                ('Part_6', models.URLField(blank=True, max_length=400, null=True)),
                ('Ad_link_1', models.URLField(blank=True, max_length=400, null=True)),
                ('Ad_link_2', models.URLField(blank=True, max_length=400, null=True)),
                ('Ad_link_3', models.URLField(blank=True, max_length=400, null=True)),
                ('published', models.BooleanField(default=False)),
                ('publish_date', models.DateField(null=True)),
                ('slug', models.SlugField(unique_for_date='publish_date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, default='BB User', max_length=40)),
                ('text', models.TextField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainapp.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, to='mainapp.choiceprogram'),
        ),
    ]