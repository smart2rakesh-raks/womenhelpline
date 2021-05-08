# Generated by Django 2.0.7 on 2018-10-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complaintstructure',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cpname', models.CharField(max_length=4000)),
                ('ctitle', models.CharField(max_length=4000)),
                ('cdes', models.CharField(max_length=20000)),
                ('cimage1', models.CharField(max_length=4000)),
                ('cimage2', models.CharField(max_length=4000)),
                ('cimage3', models.CharField(max_length=4000)),
                ('cagainstname', models.CharField(max_length=4000)),
                ('csubmiterphone', models.CharField(max_length=4000)),
            ],
            options={
                'db_table': 'complaints',
            },
        ),
    ]