from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='home'),
    path('updateTask/<task_id>', views.updateTask, name='updateTask'),
    path('deleteTask/<task_id>', views.deleteTask, name='deleteTask'),
]