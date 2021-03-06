# Generated by Django 3.0.5 on 2020-05-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_delete_scategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=250)),
                ('s_img', models.CharField(max_length=250)),
                ('s_type', models.IntegerField()),
                ('s_state', models.IntegerField()),
                ('s_short_desc', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 's_category',
                'managed': False,
            },
        ),
    ]
