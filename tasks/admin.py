from django.contrib import admin
from . models import Tasks


# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    readonly_fields = ("datecreated",)
admin.site.register(Tasks,TasksAdmin)

# Register your models here.
