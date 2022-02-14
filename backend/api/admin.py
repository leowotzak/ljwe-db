from django.contrib import admin
from .models import (
    Symbol,
    BarDataDaily,
    BarDataWeekly,
    BarDataMonthly,
    BarData1Min,
    BarData5Min,
    BarData15Min,
    BarData30Min,
    BarData1H,
)


admin.site.register(Symbol)
admin.site.register(BarDataDaily)
admin.site.register(BarDataWeekly)
admin.site.register(BarDataMonthly)
admin.site.register(BarData1Min)
admin.site.register(BarData5Min)
admin.site.register(BarData15Min)
admin.site.register(BarData30Min)
admin.site.register(BarData1H)
