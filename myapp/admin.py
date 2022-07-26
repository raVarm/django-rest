from django.contrib import admin
from . models import User_service
# Register your models here.
@admin.register(User_service)
class User_serviceAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name', 'service', 'service_man', 'date', 'check_in', 'check_out', 'cost']