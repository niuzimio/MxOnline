from django.conf.urls import url
from django.urls import path

from apps.organizations.views import OrgView, AddAskView, OrgHomeView, OrgTeacherView, OrgCourseView, OrgDescView
from apps.organizations.views import TeacherListView, TeacherDetailView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="list"),
    url(r'^add_ask/$', AddAskView.as_view(), name="add_ask"),
    # 机构列表展示
    url(r'^(?P<org_id>\d)/$', OrgHomeView.as_view(), name="home"),
    # 机构讲师
    url(r'^(?P<org_id>\d+)/teacher/$', OrgTeacherView.as_view(), name="teacher"),
    # 机构课程
    url(r'^(?P<org_id>\d+)/course/$', OrgCourseView.as_view(), name="course"),
    # 机构描述
    url(r'^(?P<org_id>\d+)/desc/$', OrgDescView.as_view(), name="desc"),
    # path('<int:org_id>/', OrgHomeView.as_view(), name="home"),


    # 讲师列表页
    url(r'^teachers/$', TeacherListView.as_view(), name="teachers"),
    url(r'^teachers/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),
]
