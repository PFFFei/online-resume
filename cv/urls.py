from django.urls import re_path,path 
from .views import *

app_name = 'cv'

urlpatterns = [
	path('list/',resume_list,name='list'),
	path('create/',create_resume,name='create'),
    re_path(r'^print/(?P<pk>\d+)/$',preview_resume,name='print'),
    re_path(r'^edit/(?P<pk>\d+)/$',preview_resume,name='edit'),
    re_path(r'^preview/(?P<pk>\d+)/$',preview_resume,name='preview'),
    re_path(r'^delete/(?P<pk>\d+)/$',delete_resume,name='delete'),

]