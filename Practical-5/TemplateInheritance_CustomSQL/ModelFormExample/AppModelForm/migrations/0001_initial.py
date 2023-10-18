# Generated by Django 3.2.5 on 2023-09-12 07:21

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
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('agree', models.BooleanField()),
            ],
            options={
                'db_table': 'AppModelForm_Student',
            },
        ),
    ]