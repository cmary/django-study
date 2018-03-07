#---encoding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class CourseListView(View):
    def get(self,request):
        courses = Course.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(courses, 2, request=request)

        course = p.page(page)

        context = {
            "courses":course

        }
        return render(request,'course-list.html',context)
