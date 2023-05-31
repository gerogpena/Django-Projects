from django.contrib import admin
from .import models

# Register your models here.

class web_crawler_admin(admin.AdminSite):
    site_header = 'Web Crawler Administration'

web_crawler_site = web_crawler_admin(name='WebCrawlerAdmin')

admin.site.register(models.Website)
web_crawler_site.register(models.Website)

admin.site.register(models.Page)
web_crawler_site.register(models.Page)

admin.site.register(models.Link)
web_crawler_site.register(models.Link)