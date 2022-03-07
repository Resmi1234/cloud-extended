from django.contrib import admin

# Register your models here.
from extendedcloudapp.models import Owner, Receiver, Upload

admin.site.register(Owner)
admin.site.register(Receiver)
admin.site.register(Upload)
