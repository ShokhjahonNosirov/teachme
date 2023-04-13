from django.urls import path
from .views import HomeView, CourseView, StoryView, CourseLessonView

app_name = 'teachme'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:course_name>/', CourseView.as_view(), name='course'),
    path('<str:course_name>/story/<str:slug>/', StoryView.as_view(), name='story'),
    path('<str:course_name>/lessons/<str:slug>/', CourseLessonView.as_view(), name='course')
]