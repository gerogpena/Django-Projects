from django.contrib import admin
from . import models

# Register your models here.

class ticket_system_admin(admin.AdminSite):
    site_header ='Ticket System Administration'

ticket_system_site = ticket_system_admin(name='TicketSysAdmin')

admin.site.register(models.ticket)
ticket_system_site.register(models.ticket)

admin.site.register(models.customer)
ticket_system_site.register(models.customer)

admin.site.register(models.comment)
ticket_system_site.register(models.comment)

admin.site.register(models.ticket_user)
ticket_system_site.register(models.ticket_user)