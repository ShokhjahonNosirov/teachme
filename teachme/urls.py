from django.urls import path
from .views import HomeView, CourseView, StoryView

app_name = 'teachme'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:course_name>/', CourseView.as_view(), name='course'),
    path('story/<int:pk>/', StoryView.as_view(), name='course')

]