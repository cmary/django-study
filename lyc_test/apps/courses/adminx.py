#---encoding=utf-8
__author__ = 'lyc'
__date__ = '18-2-27 上午11:27'

from .models import *
import xadmin

class CourseAdmin(object):

    list_display = ['course_org','name','desc','detail','is_banner','teacher','degree',
                    'learn_times','students','fav_nums','image','click_nums','category',
                    'tag','youneed_know','teacher_tell','add_time']

    search_fields =['course_org','name','desc','detail','is_banner','teacher','degree',
                    'learn_times','students','fav_nums','image','click_nums','category',
                    'tag','youneed_know','teacher_tell','add_time']

    list_filter = ['course_org','name','desc','detail','is_banner','teacher','degree',
                    'learn_times','students','fav_nums','image','click_nums','category',
                    'tag','youneed_know','teacher_tell','add_time']

class LessonAdmin(object):

    list_display = ['course','name','learn_times','add_time']
    search_fields = ['course','name','learn_times']
    list_filter = ['course__name','name','learn_times','add_time']


class VideoAdmin(object):

    list_display=['lesson','name','learn_times','url','add_time']
    search_fields= ['lesson','name','learn_times','url']
    list_filter=['lesson','name','learn_times','url','add_time']

class CourseResourceAdmin(object):
    list_display=['course','name','download','add_time']
    search_fields=['course','name','download']
    list_filter=['course','name','download','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)