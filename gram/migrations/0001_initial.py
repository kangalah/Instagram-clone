# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-13 12:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=50)),
                ('posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='text.png', upload_to='images/')),
                ('caption', models.CharField(max_length=200)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('like_add', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-date_uploaded'],
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('photo', models.ImageField(default=True, upload_to='images')),
                ('bio', tinymce.models.HTMLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.Image'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
