"""itms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from ticket_system.admin import ticket_system_site
from crawler.admin import web_crawler_site
from task_manager.admin import task_manager_site
from e_commerce.admin import store_manager_site

from pages.views import home_view, about_view, contact_view, blog_view
from ticket_system.views import create_ticket_view, tickets_list_view, ticket_detail_view, update_ticket_list, delete_ticket_list, add_ticket_comment, add_customer_list, customer_list_view
from crawler.views import crawl, show_pages
from task_manager.views import user_dashboard, create_task, delete_task, update_task, add_comment, archive_task, view_task, view_task_archives


urlpatterns = [
    # admin urls
     path('admin/', admin.site.urls),
     path('ticketsysadmin/', ticket_system_site.urls),
     path('webcrawleradmin/', web_crawler_site.urls),
     path('taskmanageradmin/', task_manager_site.urls),
     path('storemanageradmin/', store_manager_site.urls),

     # pages app urls
     path('', home_view, name='home'),
     path('about/', about_view, name='about'),
     path('contact/', contact_view, name='contact'),
     path('blog/', blog_view, name='blog'),

     #path('users/', include('django.contrib.auth.urls')),
     path('users/', include('users_account.urls')),

     # ticket app urls
     #path('tickets/', include('ticket_system.urls')),
     path('ticket/list/', tickets_list_view, name='ticket_list'),
     path('ticket/create/', create_ticket_view, name='ticket_create'),
     path('ticket/update/<str:pk>', update_ticket_list, name='ticket_update'),
     path('ticket/delete/<str:pk>', delete_ticket_list, name='ticket_delete'),
     path('ticket/detail/<str:pk>', ticket_detail_view, name='ticket_detail'),
     path('ticket/add_comment/<str:pk>', add_ticket_comment, name='ticket_comment'),
     path('ticket/add_customer/',add_customer_list, name='customer_add'),
     path('ticket/customer_list/',customer_list_view, name='customer_view'),
     
     # web crawler urls
     path('crawler/crawl/', crawl, name='crawl'),
     path('crawler/show-pages/', show_pages, name='show_pages'),

     # task manager urls
     path('task/dashboard', user_dashboard, name='user_dashboard'),
     path('task/create/', create_task, name='create_task'),
     path('task/archives/', view_task_archives, name='archives_task'),
     path('task/<int:task_id>/', view_task, name='view_task'),
     path('task/<int:task_id>/update/', update_task, name='update_task'),
     path('task/<int:task_id>/archive/', archive_task, name='archive_task'),
     path('task/<int:task_id>/delete/', delete_task, name='delete_task'),
     path('task/<int:task_id>/comment/', add_comment, name='add_comment'),

     path('store/', include('e_commerce.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
