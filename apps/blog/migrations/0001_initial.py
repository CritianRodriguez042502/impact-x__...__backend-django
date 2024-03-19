# Generated by Django 4.2.4 on 2023-09-23 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('creation', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='img_blogs')),
                ('content', models.TextField(blank=True)),
                ('public', models.BooleanField(default=False)),
                ('creation', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.categoryes')),
            ],
            options={
                'ordering': ['-creation'],
            },
        ),
    ]
