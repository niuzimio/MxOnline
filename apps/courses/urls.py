from django.conf.urls import url
from django.urls import path

from apps.courses.views import CourseListView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="list"),
    # url(r'^add_ask/$', AddAskView.as_view(), name="add_ask"),
    # # 机构详情展示
    # url(r'^(?P<org_id>\d)/$', OrgHomeView.as_view(), name="home"),
    # # 机构讲师
    # url(r'^(?P<org_id>\d+)/teacher/$', OrgTeacherView.as_view(), name="teacher"),
    # # 机构课程
    # url(r'^(?P<org_id>\d+)/course/$', OrgCourseView.as_view(), name="course"),
    # # 机构描述
    # url(r'^(?P<org_id>\d+)/desc/$', OrgDescView.as_view(), name="desc"),
    # # path('<int:org_id>/', OrgHomeView.as_view(), name="home"),
]
