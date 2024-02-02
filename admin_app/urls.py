from django.urls import path
from admin_app.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('projects/', project_list, name='project_list'),
    path('projects/add/', project_add, name='project_add'),
    path('projects/<int:project_id>/view/', project_view, name='project_view'),
    path('projects/<int:project_id>/edit/', project_edit, name='project_edit'),
    path('projects/<int:project_id>/delete/', project_delete, name='project_delete'),
    
    path('message/list/', message_list, name='message_list'),
    path('message/<int:message_id>/view', message_view, name='message_view'),
]