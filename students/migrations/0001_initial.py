# Generated by Django 4.0.1 on 2022-01-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('age', models.SmallIntegerField(verbose_name='age')),
                ('classmate', models.CharField(db_column='class', max_length=15, verbose_name='class')),
                ('description', models.TextField(blank=True, null=True, verbose_name='bio')),
            ],
            options={
                'verbose_name': 'student information',
                'verbose_name_plural': 'student information',
                'db_table': 'db_student',
            },
        ),
    ]
