from django.conf.urls import url
from django.urls import path

from MyCourse import views

# from MyCourse.views import ImageAPIView

urlpatterns = [
    url(r'^api/course/details', views.fetch_course_details),
    url(r'^api/course$', views.course_list),
    url(r'^api/course/(?P<pk>[0-9]+)$', views.course_detail),
    url(r'^api/course/online/(?P<pk>[0-9]+)$', views.course_online),
    url(r'^api/course/recovery/(?P<pk>[0-9]+)$', views.course_recovery)
]
