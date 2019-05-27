from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeesView(APIView):
    def get(self, request, pk=None):
        if pk:
            employee = get_object_or_404(Employee.objects.all(), pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response({"employee": serializer.data})
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"employees": serializer.data})

    def post(self, request):
        employee = request.data.get('employee')

        # Create an employee from the above data
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' created successfully".format(employee_saved.name)})

    def put(self, request, pk):
        saved_employee = get_object_or_404(Employee.objects.all(), pk=pk)
        data = request.data.get('employee')
        serializer = EmployeeSerializer(instance=saved_employee, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' updated successfully".format(employee_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({"message": "Employee with id `{}` has been deleted.".format(pk)},status=204)


@api_view(['POST'])
def login_user(request, pk):
    if pk:
        employee = Employee.objects.get(id=pk)
        request_data = {}
        request_data["email"] = request.data.get('username')
        request_data["password"] = request.data.get('password')
        try:
            if request_data['email'] == employee.email:
                if request_data['password'] == employee.password:
                    return Response({"message": "Employee successfully logged in"})
                else:
                    return Response({"message": "password or username incorrect"})
            else:
                return Response({"message": "password or email is incorrect"})
        except:
            return Response({"message": "Key Errors"})
    else:
        return Response({"message": "Bad request"})


@api_view(['POST'])
def logout_user(request, pk):
    employee = get_object_or_404(Employee.objects.all(), pk=pk)

    if employee:
        return Response({"message": "Employee logout successful"})
    else:
        return Response({"message": "User did not logged in"})
