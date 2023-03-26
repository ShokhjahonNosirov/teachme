from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Post
from .serializers import CourseSerializer, Course_Post_Serializer


class CourseView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseItemView(APIView):
    def get(self, request, format=None, **kwargs):
        course = Post.objects.filter(course__name=kwargs['cat_name'])
        serializer = Course_Post_Serializer(course, many=True)
        return Response(serializer.data)