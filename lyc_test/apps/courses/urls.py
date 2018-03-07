#---encoding=utf-8
__author__ = 'lyc'


from django.conf.urls import url,include
from  .views import *

urlpatterns = [
    url(r'^list/$',CourseListView.as_view(),name="org_list"),
]