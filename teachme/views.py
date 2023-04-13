from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Lesson
from .serializers import CourseSerializer, Course_Lesson_Serializer, StorySerializer


class HomeView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseView(APIView):

    def get(self, request, format=None, **kwargs):
        course = Course.objects.filter(name=kwargs['course_name'])
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

class StoryView(APIView):

    def get(self, request, format=None, **kwargs):
        video = Lesson.objects.filter(course__name=kwargs['course_name'], story_post__story_name=kwargs['slug'])
        serializer = StorySerializer(video, many=True)
        return Response(serializer.data)



class CourseLessonView(APIView):
    def get(self, request, format=None, **kwargs):
        course = Lesson.objects.filter(course__name=kwargs['course_name'], title=kwargs['slug'])
        serializer = Course_Lesson_Serializer(course, many=True)
        return Response(serializer.data)

