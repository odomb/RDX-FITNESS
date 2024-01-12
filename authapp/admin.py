from django.contrib import admin
from authapp.models import Contact,Membershipplan,Enrollment,Trainer



# Register your models here.
admin.site.register(Contact)
admin.site.register(Membershipplan)
admin.site.register(Enrollment)
admin.site.register(Trainer)