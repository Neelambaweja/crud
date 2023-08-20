from django.contrib import admin
from tabledata.models import insertdata
from tabledata.models import helpdata

# Register your models here.
class insertdataAdmin(admin.ModelAdmin):
    list_display=('name','phone','city',)
admin.site.register(insertdata,insertdataAdmin)


class helpAdmin(admin.ModelAdmin):
    list_display=('name','phone','msg',)
admin.site.register(helpdata,helpAdmin)