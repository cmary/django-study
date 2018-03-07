# encoding=utf-8
"""lyc_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView,RegisterView
from organization.views import OrgView
from django.views.static import  serve
from lyc_test.settings import MEDIA_ROOT
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',TemplateView.as_view(template_name = "index.html"),name="index"),
    url(r'^login/$',LoginView.as_view(),name="login"),
    url(r'^register/$',RegisterView.as_view(),name="register"),
    #验证码
    url(r'^captcha/',include('captcha.urls')),

    #kehcengjigou
    #url(r'^org_list/$',OrgView.as_view(),name="org_list"),
    #c处理上传文件的访问处理url
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    #URL
    url(r'^org/',include('organization.urls',namespace="org")),
    url(r'course/',include('courses.urls',namespace='course'))
]
