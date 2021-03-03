from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.static import serve
from CourseProject.settings import MEDIA_ROOT
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Course API",
        default_version='v1',
        description="Courses interfaces for API developers",
        terms_of_service="http://127.0.0.1:8080/course/index",
        contact=openapi.Contact(email="yanwun1214@gmail.com"),
        license=openapi.License('MIT License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^', include('MyCourse.urls')),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
                  url(r'^api/auth/get_token/', TokenObtainPairView.as_view()),
                  url(r'^api/auth/refresh_token/', TokenRefreshView.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
