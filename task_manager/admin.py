from django.contrib import admin
from .import models
# Register your models here.

class task_manager_admin(admin.AdminSite):
    site_header = 'Task Management Administration'

task_manager_site = task_manager_admin(name='TaskManagerAdmin')

admin.site.register(models.Task)
task_manager_site.register(models.Task)

admin.site.register(models.Comment)
task_manager_site.register(models.Comment)

admin.site.register(models.Dashboard)
task_manager_site.register(models.Dashboard)

admin.site.register(models.taskmanager_user)
task_manager_site.register(models.taskmanager_user)