from rest_framework import serializers
from .models import Course, Lesson, Answer, Question

class StorySerializer(serializers.ModelSerializer):
    story_post_video = serializers.CharField(source='story_post.video')
    class Meta:
        model = Lesson
        fields = [
            'story_post_video'
        ]

class AllStoriesSerializer (serializers.ModelSerializer):
    story_post_video = serializers.CharField(source='story_post.video')
    class Meta:
        model = Lesson
        fields = [
            'story_post_video'
        ]


class CourseSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='ca   tegory.name')

    class Meta:
        model = Course
        fields = [
            'name', 'course_image', 'about'
        ]

class Course_Lesson_Serializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name')
    # It was used to make string name the pk of course
    # story_post_name = serializers.CharField(source='story_post.story_name')

    class Meta:
        model = Lesson
        fields = [
            'title', 'video1', 'title1', 'video2', 'title2',
            'video3', 'title3', 'video4', 'title4', 'text',
            'course_name', 'story_post'
        ]



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'title', 'answer',
        ]
