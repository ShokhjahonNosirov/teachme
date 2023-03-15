from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = [
        'text',
    ]

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'text',
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
