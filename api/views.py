from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.versioning import URLPathVersioning
from api.ser import CourseSerializer
from api import models
class TestView(APIView):

    def get(self,request,*args,**kwargs):
        print(request.version)
        return Response('hello')


class CrossView(APIView):
    def get(self,request,*args,**kwargs):
        with open('crossdomain.xml') as f:
            data = f.read()
        return Response(data)


class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        result = {'code': 10000, 'data': None, 'error': None}

        queryset = models.Course.objects.all()
        ser = CourseSerializer(instance=queryset,many=True)
        result['data'] = ser.data
        return Response(result)

    def post(self, request, *args, **kwargs):
        # 1.获取用户提交的数据  request.data
        # 2.校验数据的合法性 序列化
        # 3.校验通过save
        # 4.不通过报错
        result = {'code':10000,'data':None,'error':None}

        ser = CourseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(result)

        result['error'] = ser.errors
        result['code'] = 20000
        return Response(result)


class CourseNewView(ListAPIView,CreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer



class CourseCrudView(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class CourseFileView(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        with open('crossdomain.xml') as f:
            data = f.read()
        return Response(data)












