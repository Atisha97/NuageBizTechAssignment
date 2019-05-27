from django.urls import path

from .views import EmployeesView, login_user, logout_user


app_name = "employees"


urlpatterns = [
    path('', EmployeesView.as_view()),
    path('<int:pk>', EmployeesView.as_view()),
    path('<int:pk>/login', login_user),
    path('<int:pk>/logout', logout_user)
]
