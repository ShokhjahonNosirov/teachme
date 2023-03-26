from django.urls import path
from .views import CourseView, CourseItemView

app_name = 'teachme'

urlpatterns = [
    path('', CourseView.as_view(), name='home'),
    path('<str:cat_name>/', CourseItemView.as_view(), name='course')
]