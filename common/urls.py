from django.urls import path

from common.views import *

app_name='common'

urlpatterns = [
    path('', home, name='home'),
    path('grade/', grade, name='grade'),
    path('add-grade/', add_grade, name='add-grade'),
    path('delete-grade/<int:id>/', delete_grade, name='delete-grade'),
    path('update-grade/<int:id>/', update_grade, name='update-grade'),
    path('teacher/', teacher, name='teacher'),
    path('student/', student, name='student'),
]