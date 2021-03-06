# Generated by Django 3.2.5 on 2021-11-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserVo',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('reg_date', models.DateField()),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]
