'''from django.urls import path


urlpatterns = [

] '''


'''from django.urls import path
from .views import StudentCreateView, StudentListView, StudentDeleteView, StudentUpdateView

urlpatterns = [
    path('', StudentListView.as_view(), name="student_list"),
    path('create/', StudentCreateView.as_view(), name="create_student"),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name="update_student"),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name="delete_student"),
    ]'''


from django.urls import path
from .views import (
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='addrec'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='uprec'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='deleterec'),
]

