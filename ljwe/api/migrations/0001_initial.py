# Generated by Django 3.2.9 on 2021-11-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlembicVersion',
            fields=[
                ('version_num', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'alembic_version',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarData15Min',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_15min',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarData1H',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_1h',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarData1Min',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_1min',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarData30Min',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_30min',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarData5Min',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_5min',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarDataDaily',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
                ('split_coeff', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_daily',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarDataMonthly',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_monthly',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarDataWeekly',
            fields=[
                ('timestamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('symbol_id', models.IntegerField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('adj_close_price', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('dividend_amount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_data_weekly',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Symbols',
            fields=[
                ('symbol_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=180)),
                ('ticker', models.CharField(max_length=18)),
                ('description', models.TextField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=30, null=True)),
                ('asset_type', models.CharField(blank=True, max_length=10, null=True)),
                ('created_date', models.DateTimeField()),
                ('last_updated_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'symbols',
                'managed': False,
            },
        ),
    ]
