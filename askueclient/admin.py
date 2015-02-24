from django.contrib import admin

from askueclient.models import Data30M, TimeDay

# Register your models here.


class Data30MAdmin(admin.ModelAdmin):
    list_display = ( 'point','dtime', 'param', 'zn')

class TimeDayAdmin(admin.ModelAdmin):
    list_display=('number_3min', 'number_5min', 'number_30min', 'number_1hour')

admin.site.register(Data30M, Data30MAdmin)
admin.site.register(TimeDay, TimeDayAdmin)

