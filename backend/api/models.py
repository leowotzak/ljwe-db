#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
from django.db import models


# fmt: off
class BarData15Min(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_15min"
        unique_together   = (("timestamp", "symbol"),)


class BarData1H(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_1h"
        unique_together   = (("timestamp", "symbol"),)


class BarData1Min(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_1min"
        unique_together   = (("timestamp", "symbol"),)


class BarData30Min(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_30min"
        unique_together   = (("timestamp", "symbol"),)


class BarData5Min(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_5min"
        unique_together   = (("timestamp", "symbol"),)


class BarDataDaily(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_daily"
        unique_together   = (("timestamp", "symbol"),)


class BarDataMonthly(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_monthly"
        unique_together   = (("timestamp", "symbol"),)


class BarDataWeekly(models.Model):
    timestamp         = models.DateTimeField(primary_key=True)
    symbol            = models.ForeignKey("Symbol", models.DO_NOTHING)
    open_price        = models.FloatField()
    high_price        = models.FloatField()
    low_price         = models.FloatField()
    close_price       = models.FloatField()
    adj_close_price   = models.FloatField(blank=True, null=True)
    volume            = models.IntegerField()
    dividend_amount   = models.FloatField(blank=True, null=True)
    split_coeff       = models.FloatField(blank=True, null=True)
    created_date      = models.DateTimeField(blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed           = True
        db_table          = "bar_data_weekly"
        unique_together   = (("timestamp", "symbol"),)


class Symbol(models.Model):
    symbol_id           = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=200)
    ticker              = models.CharField(max_length=30)
    description         = models.TextField(blank=True, null=True)
    sector              = models.CharField(max_length=30, blank=True, null=True)
    asset_type          = models.CharField(max_length=30, blank=True, null=True)
    created_date        = models.DateTimeField(blank=True, null=True)
    last_updated_date   = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed   = True
        db_table  = "symbol"
