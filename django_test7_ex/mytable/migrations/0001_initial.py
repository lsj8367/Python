# Generated by Django 3.1.2 on 2020-11-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buser',
            fields=[
                ('buser_no', models.IntegerField(primary_key=True, serialize=False)),
                ('buser_name', models.CharField(max_length=10)),
                ('buser_loc', models.CharField(blank=True, max_length=10, null=True)),
                ('buser_tel', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'buser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gogek',
            fields=[
                ('gogek_no', models.IntegerField(primary_key=True, serialize=False)),
                ('gogek_name', models.CharField(max_length=10)),
                ('gogek_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('gogek_jumin', models.CharField(blank=True, max_length=14, null=True)),
            ],
            options={
                'db_table': 'gogek',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jikwon',
            fields=[
                ('jikwon_no', models.IntegerField(primary_key=True, serialize=False)),
                ('jikwon_name', models.CharField(max_length=10)),
                ('buser_num', models.IntegerField()),
                ('jikwon_jik', models.CharField(blank=True, max_length=10, null=True)),
                ('jikwon_pay', models.IntegerField(blank=True, null=True)),
                ('jikwon_ibsail', models.DateField(blank=True, null=True)),
                ('jikwon_gen', models.CharField(blank=True, max_length=4, null=True)),
                ('jikwon_rating', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'jikwon',
                'managed': False,
            },
        ),
    ]
