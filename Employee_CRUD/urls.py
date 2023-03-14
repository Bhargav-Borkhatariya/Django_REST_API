from django.urls import path
from Employee_CRUD.views import EmployeeApiView

urlpatterns = [
    path('employees/', EmployeeApiView.as_view()),
    path('employees/<int:pk>/', EmployeeApiView.as_view()),
]
