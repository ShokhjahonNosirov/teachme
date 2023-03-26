from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = [
        'story_name',
        'img1',
        'text1',
        'img2',
        'text2',
        'img3',
        'text3',
        'audio_link'
    ]

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'course_image',
        'about'
    ]

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'video1',
        'title1',
        'video2',
        'title2',
        'video3',
        'title3',
        'video4',
        'title4',
        'text',
        'course',
        'story_post'
    ]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right'
    ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'post',
    ]
    list_display = [
        'title',
        'post',
    ]
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
    ]
