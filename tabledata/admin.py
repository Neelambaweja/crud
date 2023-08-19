from django.contrib import admin
from tabledata.models import insertdata

# Register your models here.
class insertdataAdmin(admin.ModelAdmin):
    list_display=('name','phone','city',)

admin.site.register(insertdata,insertdataAdmin)