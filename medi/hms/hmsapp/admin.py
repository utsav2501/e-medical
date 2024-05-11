from django.contrib import admin

# Register your models here.


from .models import student
from .models import record
from .models import reguser

admin.site.register(student)
admin.site.register(record)
admin.site.register(reguser)