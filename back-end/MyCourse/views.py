from django.shortcuts import render
from django.http.response import JsonResponse
# Restful framwork
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Course API
from MyCourse.models import Course
from MyCourse.serializers import CourseSerializer
# Jwt
from rest_framework.permissions import IsAuthenticated
# Swagger
from drf_yasg.utils import swagger_auto_schema
# Ratelimit



@swagger_auto_schema(operation_summary="取得課程全部相關資訊",
                     operation_description='此接口為前後台取得課程資料的接口，本系統有做"soft delete，所以需有權限才可以取得刪除後的資訊。',
                     method="GET")
@api_view(['GET'])
def fetch_course_details(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        # 抓course的name作為檢查項目
        name = request.GET.get('name', None)
        # find by course_name
        if name is not None:
            courses = courses.filter(name__icontains=name)
        courses_serializers = CourseSerializer(courses, many=True)
        return JsonResponse(courses_serializers.data, safe=False)


@swagger_auto_schema(operation_summary="新增課程資料",
                     operation_description='新增課程資料',
                     method="POST",
                     request_body=CourseSerializer)
@swagger_auto_schema(operation_summary="刪除全部資料",
                     operation_description='刪除資料庫所有的課程資料！，因為風險過高所以只有最高權限者可以使用',
                     method="DELETE",
                     deprecated=True)
@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        # 抓course的name作為檢查項目
        name = request.GET.get('name', None)
        # find by course_name
        if name is not None:
            courses = courses.filter(name__icontains=name)
        courses_serializers = CourseSerializer(courses, many=True)
        return JsonResponse(courses_serializers.data, safe=False)

    elif request.method == 'POST':
        # course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(data=request.data)
        print(request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse(course_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Course.objects.all().delete()
        return JsonResponse({'message': '{} Courses were all deleted successfully!'.format(count[0])})



@swagger_auto_schema(operation_summary="利用課程id取得相對應資訊",
                     operation_description='此接口為後台取得課程資料的接口。',
                     method="GET")
@swagger_auto_schema(operation_summary="更新課程資訊by ID",
                     operation_description='此接口為後台更新資料的接口',
                     method="PUT",
                     request_body=CourseSerializer)
@swagger_auto_schema(operation_summary="根據課程id刪除課程資訊，此為soft-delete接口",
                     operation_description='此接口為後台刪除『顯示』資料的接口，若要復原可以請求最高權限者。',
                     method="DELETE")
@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        if request.method == "GET":
            course_serializer = CourseSerializer(course)
            return JsonResponse(course_serializer.data)
        elif request.method == "PUT":
            modify_course = Course.objects.filter(id__contains=request.data['id'])
            # print(request.data['name'])
            if (request.data['id'] != None):
                # print('hi')
                modify_course.update(name=request.data['name'],
                                     teacher=request.data['teacher'],
                                     loc=request.data['loc'],
                                     content=request.data['content'],
                                     date=request.data['date'],
                                     )
                return JsonResponse({'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'message': 'Updated failed'}, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            # 做soft delete
            # sys = 0表示已刪除 不要刪除資料庫資料
            if course.sys == 0 or course.sys == "":
                return JsonResponse({'message': 'course was already deleted!!'}, status=status.HTTP_204_NO_CONTENT)
            else:
                my_course = Course.objects.filter(id__contains=course.pk)
                my_course.update(sys=0)
                # course.delete()，真的要刪除才使用此項目
                return JsonResponse({'message': 'course was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Course.DoesNotExist:
        return JsonResponse({'message': 'The course does not exist'}, status=status.HTTP_404_NOT_FOUND)



@swagger_auto_schema(operation_summary="取得有『上架』課程的資訊",
                     operation_description='此接口為管理者方便取得有上架的資訊',
                     method="GET")
@swagger_auto_schema(operation_summary="根據id迅速更新是否上架流程",
                     operation_description='此接口為後台管理者方便迅速更新上架資訊。',
                     method="PUT")
@api_view(['GET', 'PUT'])
def course_online(request, pk):
    courses = Course.objects.filter(online=True)
    if request.method == 'GET':
        courses_serializer = CourseSerializer(courses, many=True)
        return JsonResponse(courses_serializer.data, safe=False)

    elif request.method == 'PUT':
        course = Course.objects.get(pk=pk)
        modify_course = Course.objects.filter(id__contains=course.pk)
        modify_course.update(online=not course.online)
        return JsonResponse({'message': 'Updated Successfully'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'message': 'Updated fails'}, status=status.HTTP_404_NOT_FOUND)
