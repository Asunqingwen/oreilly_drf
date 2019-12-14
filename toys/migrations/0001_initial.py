# Generated by Django 3.0 on 2019-12-14 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('toy_category', models.CharField(blank=True, default='', max_length=200)),
                ('release_date', models.DateTimeField()),
                ('was_included_in_home', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
