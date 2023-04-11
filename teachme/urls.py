from django.urls import path
from .views import HomeView, CourseView

app_name = 'teachme'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:cat_name>/', CourseView.as_view(), name='course')
]