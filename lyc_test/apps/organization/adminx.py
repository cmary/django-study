#---encoding=utf-8
__author__ = 'lyc'
__date__ = '18-2-27 下午3:22'

import xadmin
from .models import *

class CourseOrgAdmin(object):

    list_display = ['name','desc','tag','category','click_nums','fav_nums','image','address','students','course_nums','add_time']
    search_fields = ['name','desc','tag','category','click_nums','fav_nums','image','address','students','course_nums']
    list_filter = ['name','desc','tag','category','click_nums','fav_nums','image','address','students','course_nums','add_time']


class TeacherAdmin(object):

    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'age',
                    'image', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'age',
                    'image', 'add_time']
    list_filter =['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'age',
                    'image', 'add_time']

class CityDictAadmin(object):

    list_display = ['name', 'desc', 'work_years', 'add_time']
    search_fields = ['name', 'desc', 'work_years', 'add_time']
    list_filter = ['name', 'desc', 'work_years', 'add_time']

xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CityDict,CityDictAadmin)