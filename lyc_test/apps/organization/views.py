#encoding=utf8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from forms import UserAskForm
from operation.models import UserFavorite
from courses.models import Course
#from utils.mixin_utils import LoginRequiredMixin
# Create your views here.

class OrgView(View):
    '''课程机构'''
    def get(self,request):
        all_org = CourseOrg.objects.all()
        all_citys = CityDict.objects.all()
        org_nums = all_org.count()
        all_students = 0
        all_courses = 0

        city_id = request.GET.get("city","")

        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

        category= request.GET.get("ct","")
        if category:
            all_org = all_org.filter(category=category)

        for org in all_org:
            all_students =all_students + org.students
            all_courses = all_courses +org.course_nums

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, 2, request=request)

        orgs = p.page(page)



        context = {"all_orgs": orgs, "all_citys": all_citys,
                   "org_nums": org_nums, "all_students": all_students,
                   "all_courses": all_courses,"category":category,
                   "city_id":city_id}

        return render(request,"org_list.html",context)


class AddUserAskView(View):
    '''用户添加咨询'''

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums +=1
        course_org.save()
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        context = {
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'org':course_org,
        }
        return render(request, 'org-detail-homepage.html',context)


class OrgCourseView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()
        all_courses = course_org.course_set.all()

        context = {
            'all_courses': all_courses,
            'org': course_org,
        }
        return render(request, 'org-detail-course.html', context)



class OrgDescView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        context = {

            'org': course_org,
        }
        return render(request, 'org-detail-desc.html', context)


class OrgTeacherView(View):
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()
        all_teachers = course_org.teacher_set.all()[:1]
        context = {
            'all_teachers': all_teachers,
            'org': course_org,
        }
        return render(request, 'org-detail-teachers.html', context)


class AddFavView(View):
    '''用户收藏'''
    def post(self,request):
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)
        user = request.user
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        exist_records = UserFavorite.objects.filter(user = request.user,fav_id = int(fav_id),fav_type=int(fav_type))

        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status":"success", "msg":"已取消收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}',content_type='applicaton/json')

